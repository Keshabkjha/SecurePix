document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll("form");

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

    function previewImage(file, container) {
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function (e) {
            container.innerHTML = `<img src="${e.target.result}" alt="Preview" />`;
        };
        reader.readAsDataURL(file);
    }
});
