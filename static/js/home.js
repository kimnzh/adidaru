document.addEventListener("DOMContentLoaded", function () {
  // --- CONFIGURATION ---
  const PRODUCT_API_ENDPOINT = "/json/";
  const ADD_PRODUCT_URL = "/product/add/";
  const EDIT_PRODUCT_BASE_URL = "/product/edit/";
  const DELETE_PRODUCT_BASE_URL = "/product/delete/";
  const CURRENT_USER_ID = document.body.dataset.userId || "";

  // --- DOM ELEMENTS ---
  const loadingSpinner = document.getElementById("loading");
  const errorMessage = document.getElementById("error");
  const emptyStateDisplay = document.getElementById("empty");
  const productGridContainer = document.getElementById("grid");
  const featuredGridContainer = document.getElementById("featured-grid");
  const productForm = document.getElementById("productForm");
  const filterButtons = document.querySelectorAll(".filter-btn");
  const categoryFilterButtons = document.querySelectorAll(".filter-btn-category");
  const cartCount = document.getElementById("cart-count");

  // --- STATE ---
  let activeOwnershipFilter = "all";
  let activeCategoryFilter = "ALL";
  let allProductsData = [];

  // --- FUNCTIONS ---
  function displayPageSection({
    showLoading = false,
    showError = false,
    showEmpty = false,
    showGrid = false,
  }) {
    loadingSpinner.classList.toggle("hidden", !showLoading);
    errorMessage.classList.toggle("hidden", !showError);
    emptyStateDisplay.classList.toggle("hidden", !showEmpty);
    productGridContainer.classList.toggle("hidden", !showGrid);
  }

  function openAddModal() {
    productForm.reset();
    document.getElementById("productId").value = "";
    document.getElementById("modal-title").innerText = "Create New Product";
    document.getElementById("modal-description").innerText =
      "Fill in the details to add a new product.";
    document.getElementById("submitProduct").innerText = "Add Product";
    document
      .getElementById("submitProduct")
      .classList.remove("bg-indigo-500", "hover:bg-indigo-600");
    document
      .getElementById("submitProduct")
      .classList.add("bg-emerald-500", "hover:bg-emerald-600");
    showModal();
  }
  window.openAddModal = openAddModal;

  function openEditModal(productId) {
    const product = allProductsData.find((p) => p.id === productId);
    if (!product) {
      showToast("Error", "Product not found.", "error");
      return;
    }
    productForm.reset();
    document.getElementById("productId").value = product.id;
    document.getElementById("name").value = product.name;
    document.getElementById("price").value = product.price;
    document.getElementById("description").value = product.description;
    document.getElementById("category").value = product.category;
    document.getElementById("thumbnail").value = product.thumbnail;
    document.getElementById("stock").value = product.stock;
    document.getElementById("is_featured").checked = product.is_featured;

    document.getElementById("modal-title").innerText = "Edit Product";
    document.getElementById("modal-description").innerText = "Update the details of the product.";
    document.getElementById("submitProduct").innerText = "Save Changes";
    document
      .getElementById("submitProduct")
      .classList.remove("bg-emerald-500", "hover:bg-emerald-600");
    document.getElementById("submitProduct").classList.add("bg-indigo-500", "hover:bg-indigo-600");
    showModal();
  }

  function buildProductCardElement(productItem) {
    const productElement = document.createElement("div");
    productElement.className =
      "bg-white rounded-xl shadow-md overflow-hidden transform hover:-translate-y-1 transition-transform duration-300 flex flex-col group";

    const detailLink = `/product/${productItem.id}/`;

    const thumbnailHtml = productItem.thumbnail
      ? `<img src='${productItem.thumbnail}' alt='${productItem.name}' class='w-full h-56 object-cover group-hover:scale-105 transition-transform duration-300'>`
      : `<div class='w-full h-56 bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center'><i data-lucide="image-off" class="text-gray-400 w-16 h-16"></i></div>`;

    const editDeleteButtons =
      CURRENT_USER_ID && Number(CURRENT_USER_ID) === Number(productItem.user_id)
        ? `<div class='absolute top-3 right-3 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300'>
            <button data-action="edit" data-product-id="${productItem.id}" class="z-10 relative bg-white/80 backdrop-blur-sm rounded-full p-2 hover:bg-white transition-colors">
              <i data-lucide="square-pen" class="text-indigo-500 w-5 h-5 pointer-events-none"></i>
            </button>
            <button data-action="delete" data-product-id="${productItem.id}" class="z-10 relative bg-white/80 backdrop-blur-sm rounded-full p-2 hover:bg-white transition-colors">
              <i data-lucide="trash-2" class="text-red-500 w-5 h-5 pointer-events-none"></i>
            </button>
          </div>`
        : "";

    productElement.innerHTML = `
      <a href="${detailLink}" class="flex flex-col flex-grow">
        <div class="relative overflow-hidden">
          ${thumbnailHtml}
          ${editDeleteButtons}
        </div>
        <div class="p-5 flex flex-col flex-grow">
          <h3 class="text-lg font-semibold text-gray-800 truncate">${productItem.name}</h3>
          <p class="text-emerald-600 text-sm mt-1 font-medium">${productItem.category}</p>
          <div class="flex-grow"></div>
          <div class="flex justify-between items-center mt-4">
            <p class="text-xl font-bold text-indigo-600">Rp${productItem.price.toLocaleString(
              "id-ID"
            )}</p>
            ${
              CURRENT_USER_ID && Number(CURRENT_USER_ID) !== Number(productItem.user_id)
                ? `<button onclick="event.stopPropagation(); event.preventDefault(); addToCart(${productItem.id});" class="bg-emerald-50 text-emerald-600 px-3 py-2 rounded-lg hover:bg-emerald-100 transition-colors">
                      <i data-lucide="plus" class="w-5 h-5"></i>
                  </button>`
                : ""
            }
          </div>
        </div>
      </a>`;
    return productElement;
  }

  function renderProductCards(container, productItems) {
    container.innerHTML = "";
    productItems.forEach((productItem) => {
      const cardElement = buildProductCardElement(productItem);
      container.appendChild(cardElement);
    });
    lucide.createIcons();
  }

  function updateFilterButtonsAppearance() {
    // Ownership filters
    filterButtons.forEach((button) => {
      const filterValue = button.getAttribute("data-filter-value");
      if (filterValue === activeOwnershipFilter) {
        button.className =
          "filter-btn bg-emerald-500 text-white px-4 py-2 rounded-lg font-medium transition-colors hover:bg-emerald-600";
      } else {
        button.className =
          "filter-btn bg-white text-gray-700 border border-gray-300 px-4 py-2 rounded-lg font-medium transition-colors hover:bg-emerald-500 hover:text-white";
      }
    });

    // Category filters
    categoryFilterButtons.forEach((button) => {
      const filterValue = button.getAttribute("data-filter-value");
      if (filterValue === activeCategoryFilter) {
        button.className =
          "filter-btn-category bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full font-medium text-sm transition-colors hover:bg-emerald-200";
      } else {
        button.className =
          "filter-btn-category bg-white text-gray-600 px-3 py-1 rounded-full font-medium text-sm transition-colors hover:bg-emerald-100";
      }
    });
  }

  function filterAndDisplayProducts() {
    updateFilterButtonsAppearance();

    let filteredProducts = allProductsData;

    // Filter by ownership
    if (activeOwnershipFilter === "my") {
      filteredProducts = filteredProducts.filter(
        (p) => Number(p.user_id) === Number(CURRENT_USER_ID)
      );
    }

    // Filter by category
    if (activeCategoryFilter !== "ALL") {
      filteredProducts = filteredProducts.filter((p) => p.category === activeCategoryFilter);
    }

    if (filteredProducts.length === 0) {
      displayPageSection({ showEmpty: true });
    } else {
      renderProductCards(productGridContainer, filteredProducts);
      displayPageSection({ showGrid: true });
    }
  }

  async function fetchProductsFromServer() {
    try {
      displayPageSection({ showLoading: true });
      const response = await fetch(PRODUCT_API_ENDPOINT);
      if (!response.ok) throw new Error("Network response was not ok.");
      const productData = await response.json();
      allProductsData = productData || [];

      const featuredProducts = allProductsData.filter((p) => p.is_featured);
      renderProductCards(featuredGridContainer, featuredProducts);

      filterAndDisplayProducts();
    } catch (error) {
      console.error("Error loading products:", error);
      displayPageSection({ showError: true });
    }
  }

  window.addToCart = async function (productId) {
    try {
      const response = await fetch(`/add-to-cart/${productId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      const result = await response.json();
      if (result.status === "success") {
        showToast("Success", "Product added to cart!", "success");
        cartCount.innerText = result.cart_total;
      } else {
        showToast("Error", result.message || "An error occurred.", "error");
      }
    } catch (error) {
      showToast("Error", "An unexpected network error occurred.", "error");
    }
  };

  // --- EVENT LISTENERS ---
  productForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    const productId = formData.get("productId");
    const isEdit = productId && productId !== "";
    const url = isEdit ? `${EDIT_PRODUCT_BASE_URL}${productId}/` : ADD_PRODUCT_URL;

    try {
      const response = await fetch(url, {
        method: "POST",
        body: new URLSearchParams(formData),
        headers: {
          "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      const result = await response.json();
      if (result.status === "success") {
        hideModal();
        showToast("Success", `Product ${isEdit ? "updated" : "added"} successfully!`, "success");
        fetchProductsFromServer();
      } else {
        showToast("Error", result.message || "An error occurred.", "error");
      }
    } catch (error) {
      showToast("Error", "An unexpected network error occurred.", "error");
    }
  });

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      activeOwnershipFilter = button.getAttribute("data-filter-value");
      filterAndDisplayProducts();
    });
  });

  categoryFilterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      activeCategoryFilter = button.getAttribute("data-filter-value");
      filterAndDisplayProducts();
    });
  });
});

function openDeleteModal(productId) {
  showDeleteModal();
  const confirmDeleteButton = document.getElementById("confirmDeleteButton");
  confirmDeleteButton.onclick = async function () {
    const url = `/product/delete/${productId}/`;
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      const result = await response.json();
      if (result.status === "success") {
        hideDeleteModal();
        showToast("Success", "Product deleted successfully!", "success");
        // Re-fetch products after deletion
        if (typeof fetchProductsFromServer === "function") {
          fetchProductsFromServer();
        } else {
          window.location.reload();
        }
      } else {
        hideDeleteModal();
        showToast("Error", result.message || "An error occurred.", "error");
      }
    } catch (error) {
      hideDeleteModal();
      showToast("Error", "An unexpected network error occurred.", "error");
    }
  };
}

function openEditModal(productId) {
  const product = allProductsData.find((p) => p.id === productId);
  if (!product) {
    showToast("Error", "Product not found.", "error");
    return;
  }
  const productForm = document.getElementById("productForm");
  productForm.reset();
  document.getElementById("productId").value = product.id;
  document.getElementById("name").value = product.name;
  document.getElementById("price").value = product.price;
  document.getElementById("description").value = product.description;
  document.getElementById("category").value = product.category;
  document.getElementById("thumbnail").value = product.thumbnail;
  document.getElementById("stock").value = product.stock;
  document.getElementById("is_featured").checked = product.is_featured;

  document.getElementById("modal-title").innerText = "Edit Product";
  document.getElementById("modal-description").innerText = "Update the details of the product.";
  document.getElementById("submitProduct").innerText = "Save Changes";
  document
    .getElementById("submitProduct")
    .classList.remove("bg-emerald-500", "hover:bg-emerald-600");
  document.getElementById("submitProduct").classList.add("bg-indigo-500", "hover:bg-indigo-600");
  showModal();
}

document.addEventListener("DOMContentLoaded", function () {
  // ... (rest of the DOMContentLoaded code)

  function handleGridClick(event) {
    const button = event.target.closest("[data-action]");
    if (!button) return;

    const action = button.dataset.action;
    const productId = button.dataset.productId;

    console.log("Button clicked!", { action, productId });

    if (!action || !productId) return;

    event.preventDefault();
    event.stopPropagation();

    if (action === "edit") {
      openEditModal(productId);
    } else if (action === "delete") {
      openDeleteModal(productId);
    }
  }

  document.body.addEventListener("click", handleGridClick);

  // --- INITIALIZATION ---
  fetchProductsFromServer();
});
