import cv2
import numpy as np
import hashlib
import os
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load ResNet50 model globally
model = ResNet50(weights='imagenet')

# Label to domain mapping
label_to_domain = {
    "stethoscope": "Medical", "syringe": "Medical", "hospital": "Medical", "MRI": "Medical",
    "CT scanner": "Medical", "x-ray": "Medical", "bandage": "Medical", "first-aid kit": "Medical",
    "medical bag": "Medical", "oxygen mask": "Medical", "surgical mask": "Medical", "gown": "Medical",
    "thermometer": "Medical", "pill bottle": "Medical", "stretcher": "Medical", "wheelchair": "Medical",
    "microscope": "Medical", "scalpel": "Medical", "defibrillator": "Medical", "IV bag": "Medical",
    "security camera": "Surveillance", "CCTV": "Surveillance", "surveillance camera": "Surveillance",
    "police car": "Surveillance", "police van": "Surveillance", "handcuffs": "Surveillance",
    "baton": "Surveillance", "riot shield": "Surveillance", "drone": "Surveillance",
    "bulletproof vest": "Surveillance", "guard dog": "Surveillance", "watchtower": "Surveillance",
    "binoculars": "Surveillance", "night vision goggles": "Surveillance", "alarm system": "Surveillance",
    "metal detector": "Surveillance",
    "courthouse": "Legal", "gavel": "Legal", "judge's bench": "Legal", "law book": "Legal",
    "scales of justice": "Legal", "legal document": "Legal", "briefcase": "Legal", "courtroom": "Legal",
    "police badge": "Legal", "prison cell": "Legal", "fingerprint": "Legal", "mugshot": "Legal",
    "legal robe": "Legal", "subpoena": "Legal", "warrant": "Legal",
    "safe": "Finance", "vault": "Finance", "ATM": "Finance", "credit card": "Finance",
    "cash register": "Finance", "piggy bank": "Finance", "bank building": "Finance",
    "stock ticker": "Finance", "gold bars": "Finance", "coin stack": "Finance", "checkbook": "Finance",
    "calculator": "Finance", "ledger": "Finance", "money bag": "Finance", "wallet": "Finance",
    "receipt": "Finance",
    "lock": "Personal Privacy", "key": "Personal Privacy", "password pad": "Personal Privacy",
    "fingerprint scanner": "Personal Privacy", "face recognition": "Personal Privacy",
    "privacy screen": "Personal Privacy", "envelope": "Personal Privacy", "diary": "Personal Privacy",
    "personal ID": "Personal Privacy", "mailbox": "Personal Privacy", "curtain": "Personal Privacy",
    "door lock": "Personal Privacy", "safe deposit box": "Personal Privacy", "security token": "Personal Privacy",
    "privacy filter": "Personal Privacy"
}

# Hash and generate parameters from password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_parameters_from_password(password_hash):
    parts = [int(password_hash[i:i+8], 16) for i in range(0, 64, 8)]
    norm = lambda x: (x % 1000) / 1000
    r = 3.57 + norm(parts[0]) * (4.0 - 3.57)
    x0 = norm(parts[1])
    K = 0.3 + norm(parts[2]) * 1.2
    u = 0.7 + norm(parts[3]) * 0.3
    ikeda_x0 = norm(parts[4])
    ikeda_y0 = norm(parts[5])
    seed_mix = norm(parts[6]) + norm(parts[7])
    return r, x0, K, u, ikeda_x0, ikeda_y0, seed_mix

# Chaotic maps
def logistic_map(r, x0, size):
    x = np.zeros(size)
    x[0] = x0
    for i in range(1, size):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x

def circle_map(x0, K, size):
    x = np.zeros(size)
    x[0] = x0
    for i in range(1, size):
        x[i] = (x[i-1] + K - (0.5 / np.pi) * np.sin(2 * np.pi * x[i-1])) % 1
    return x

def ikeda_map(u, x0, y0, size):
    x = np.zeros(size)
    y = np.zeros(size)
    x[0], y[0] = x0, y0
    for i in range(1, size):
        t = 0.4 - 6 / (1 + x[i-1]**2 + y[i-1]**2)
        x[i] = 1 + u * (x[i-1] * np.cos(t) - y[i-1] * np.sin(t))
        y[i] = u * (x[i-1] * np.sin(t) + y[i-1] * np.cos(t))
    return x

# Generate key
def generate_chaotic_key(img_shape, password):
    pw_hash = hash_password(password)
    r, x0, K, u, ikeda_x0, ikeda_y0, seed_mix = generate_parameters_from_password(pw_hash)
    size = img_shape[0] * img_shape[1] * img_shape[2]
    log_map = logistic_map(r, x0, size)
    cir_map = circle_map(x0, K, size)
    ike_map = ikeda_map(u, ikeda_x0, ikeda_y0, size)
    chaotic_key = (log_map + cir_map + np.abs(ike_map)) % 1
    chaotic_key = np.floor(chaotic_key * 256).astype(np.uint8)
    return chaotic_key.reshape(img_shape)

# Encryption / Decryption
def xor_image(img, key):
    return cv2.bitwise_xor(img, key)

# Image domain prediction
def predict_image_label(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    label = decode_predictions(preds, top=1)[0][0][1]
    return label

def get_domain_from_label(label):
    return label_to_domain.get(label.lower(), "Unknown")

# Workflow wrappers
def encrypt_image_flow(img_path, password):
    label = predict_image_label(img_path)
    domain = get_domain_from_label(label)
    print(f"[INFO] Detected domain: {domain} ({label})")

    img = cv2.imread(img_path)
    img = cv2.resize(img, (256, 256))
    key = generate_chaotic_key(img.shape, password)
    enc_img = xor_image(img, key)

    # Create output path with .png extension
    base_path = os.path.splitext(img_path)[0]
    output_path = f"{base_path}_enc.png"
    cv2.imwrite(output_path, enc_img)
    return output_path

def decrypt_image_flow(img_path, password):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (256, 256))
    key = generate_chaotic_key(img.shape, password)
    dec_img = xor_image(img, key)

    # Create output path with .png extension
    base_path = os.path.splitext(img_path)[0]
    output_path = f"{base_path}_dec.png"
    cv2.imwrite(output_path, dec_img)
    return output_path
