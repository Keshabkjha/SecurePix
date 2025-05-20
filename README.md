# SecurePix - Intelligent Image Encryption and Classification System

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Deployed](https://img.shields.io/badge/Deployed-on%20Render-orange.svg)](https://securepix.onrender.com/)

## Overview
SecurePix is an advanced image encryption and classification system that combines state-of-the-art encryption techniques with intelligent image classification. This web application provides a secure way to encrypt and decrypt images while automatically categorizing them based on their content.




https://github.com/user-attachments/assets/98578b62-6216-4bce-be77-d618c7b839e3



## Key Features

- **Advanced Image Encryption**: 
  - AES-256 encryption algorithm for maximum security
  - Password-based key derivation using PBKDF2
  - Secure key management system with salt and iteration
  - Protection against brute-force attacks

- **Intelligent Image Classification**: 
  - Deep Learning-based image recognition using TensorFlow
  - Pre-trained CNN models for accurate classification
  - Automatic domain categorization (e.g., medical, legal, personal)
  - Real-time image analysis with confidence scores

- **User-Friendly Interface**: 
  - Clean and intuitive web interface built with Bootstrap
  - Drag-and-drop file upload functionality
  - Real-time encryption/decryption status indicators
  - Responsive design for all devices

- **Security Features**: 
  - End-to-end encryption
  - Secure password handling with hashing
  - Protected file storage with access controls
  - Prevention of unauthorized access attempts
  - Automatic session timeout

## Technical Architecture

### Backend Components
- **Main Application**: Flask web server handling all HTTP requests
- **Encryption Module**: Custom implementation of AES-256 encryption
- **Image Processing**: OpenCV for image preprocessing
- **Machine Learning**: TensorFlow/Keras for image classification
- **File Management**: Secure file handling and storage

### Frontend Components
- **User Interface**: Modern HTML5/CSS3 interface
- **JavaScript**: Interactive features and validation
- **Bootstrap**: Responsive design framework
- **AJAX**: Asynchronous file uploads and processing

## Why SecurePix?

In today's digital age, protecting sensitive images is crucial. SecurePix addresses this need by:

- Providing military-grade encryption for sensitive images
- Automatically categorizing images based on content
- Ensuring secure storage and transmission
- Offering a user-friendly interface for encryption/decryption
- Maintaining data privacy and integrity

## Target Users

SecurePix is ideal for:

- **Individuals**: Protecting personal photos and documents
- **Businesses**: Securing confidential product images and documents
- **Medical Professionals**: Storing sensitive medical images
- **Legal Professionals**: Protecting legal documents and evidence
- **Organizations**: Handling sensitive visual data
- **Photographers**: Protecting intellectual property

## Use Cases

1. **Personal Security**:
   - Encrypting personal photos before cloud storage
   - Protecting sensitive family images
   - Secure sharing of personal images
   - Backing up important documents

2. **Business Applications**:
   - Protecting confidential product images
   - Secure storage of business documents
   - Protecting intellectual property
   - Secure file sharing between departments
   - Client document management

3. **Professional Use**:
   - Secure storage of medical images
   - Protecting legal documents
   - Secure image sharing between professionals
   - Intellectual property protection
   - Secure document archiving

## Technologies Used

- **Backend**: 
  - Flask (Web Framework)
  - Python 3.8+
  - TensorFlow & Keras (AI/ML)
  - OpenCV (Image Processing)
  - NumPy (Numerical Computing)
  - Gunicorn (Production WSGI server)

- **Frontend**: 
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  - AJAX

- **Deployment**:
  - Render platform
  - Docker containerization
  - Automated deployment pipeline

## Live Demo

The application is live and available at: [https://securepix.onrender.com/](https://securepix.onrender.com/)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Keshabkjha/SecurePix.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Usage Guide

1. **Encrypting Images**:
   - Visit the website or run locally
   - Click on "Encrypt Image"
   - Drag and drop or select your image file
   - Enter a secure password (minimum 8 characters)
   - Click "Encrypt"
   - Download the encrypted image
   - Note: Keep the password safe as it's needed for decryption

2. **Decrypting Images**:
   - Visit the website or run locally
   - Click on "Decrypt Image"
   - Upload the encrypted image file
   - Enter the correct password used during encryption
   - Click "Decrypt"
   - Download the original image

## Security Best Practices

1. **Password Security**:
   - Use strong passwords with a mix of characters
   - Never reuse passwords
   - Store passwords securely
   - Change passwords periodically

2. **File Security**:
   - Keep encrypted files in a secure location
   - Regularly backup important files
   - Verify file integrity after encryption/decryption
   - Use secure file transfer methods

3. **System Security**:
   - Keep software updated
   - Use antivirus protection
   - Enable firewall
   - Regular security audits

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact:
- Email: keshabkumarjha876@gmail.com
- GitHub: [Keshabkjha](https://github.com/Keshabkjha)

## Acknowledgments

- TensorFlow team for their excellent ML framework
- Flask community for the web framework
- OpenCV developers for image processing capabilities
- All contributors who helped with this project
- Render platform for hosting the application

---

*Last Updated: May 2025*
