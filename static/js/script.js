document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");
    document.body.style.opacity = 0;
    setTimeout(() => {
        document.body.style.transition = "opacity 0.6s ease";
        document.body.style.opacity = 1;
    }, 100);
    window.addEventListener("pageshow", () => {
        hideLoader();
    });

    // Attach event listener for flash messages if rendered via Flask
    const toastData = document.getElementById("toast").dataset;
    if (toastData.message) {
        showToast(toastData.message, toastData.type === "error");
    }
    forms.forEach(form => {
        const fileInput = form.querySelector('input[type="file"]');
        const previewContainer = form.querySelector('.image-preview');

        fileInput.addEventListener("change", function () {
            previewImage(this.files[0], previewContainer);
        });

        form.addEventListener("dragover", (e) => {
            e.preventDefault();
            form.classList.add("dragging");
        });

        form.addEventListener("dragleave", () => {
            form.classList.remove("dragging");
        });

        form.addEventListener("drop", (e) => {
            e.preventDefault();
            form.classList.remove("dragging");
            const file = e.dataTransfer.files[0];
            if (file && file.type.startsWith("image/")) {
                fileInput.files = e.dataTransfer.files;
                previewImage(file, previewContainer);
            }
        });
    });


    // Show the loader overlay
function showLoader() {
    const loader = document.getElementById("loader");
    loader.classList.remove("hidden");
}

// Hide loader overlay
function hideLoader() {
    const loader = document.getElementById("loader");
    loader.classList.add("hidden");
}

// Show toast notification
function showToast(message, isError = false) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.style.backgroundColor = isError ? "#e53935" : "#1a73e8";
    toast.style.display = "block";

    // Auto-hide after 4 seconds
    setTimeout(() => {
        toast.style.display = "none";
    }, 4000);
}


    function previewImage(input, previewId) {
        const preview = document.getElementById(previewId);
        preview.innerHTML = "";
    
        if (input.files && input.files[0]) {
            const img = document.createElement("img");
            img.src = URL.createObjectURL(input.files[0]);
            img.onload = () => URL.revokeObjectURL(img.src);
            img.style.maxWidth = "100%";
            img.style.maxHeight = "200px";
            img.style.borderRadius = "12px";
            img.style.marginTop = "10px";
            preview.appendChild(img);
        }
    }
});
const themeToggle = document.getElementById("theme-toggle");
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
}

themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const newTheme = document.body.classList.contains("dark-mode") ? "dark" : "light";
    localStorage.setItem("theme", newTheme);
});
