function showModal() {
  const modal = document.getElementById("crudModal");
  const modalContent = document.getElementById("crudModalContent");

  modal.classList.remove("hidden");
  setTimeout(() => {
    modalContent.classList.remove("opacity-0", "scale-95");
    modalContent.classList.add("opacity-100", "scale-100");
  }, 50);
}

function hideModal() {
  const modal = document.getElementById("crudModal");
  const modalContent = document.getElementById("crudModalContent");

  modalContent.classList.remove("opacity-100", "scale-100");
  modalContent.classList.add("opacity-0", "scale-95");

  setTimeout(() => {
    modal.classList.add("hidden");
  }, 150);
}

function showDeleteModal() {
  const modal = document.getElementById("deleteConfirmationModal");
  modal.classList.remove("hidden");
}

function hideDeleteModal() {
  const modal = document.getElementById("deleteConfirmationModal");
  modal.classList.add("hidden");
}

function togglePasswordVisibility(fieldId) {
  const passwordField = document.getElementById(fieldId);
  const icon = passwordField.nextElementSibling.querySelector("i");
  if (passwordField.type === "password") {
    passwordField.type = "text";
    icon.setAttribute("data-lucide", "eye-off");
  } else {
    passwordField.type = "password";
    icon.setAttribute("data-lucide", "eye");
  }
  lucide.createIcons();
}
