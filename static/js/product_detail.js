document.addEventListener("DOMContentLoaded", function () {
  // --- CONFIGURATION ---
  const PRODUCT_DETAIL_ENDPOINT = `/json/${PRODUCT_ID}/`;
  const ADD_TO_CART_ENDPOINT = `/add-to-cart/${PRODUCT_ID}/`;

  // --- DOM ELEMENTS ---
  const loadingState = document.getElementById("loading-state");
  const errorState = document.getElementById("error-state");
  const productContent = document.getElementById("product-content");
  const badgesContainer = document.getElementById("badges-container");
  const productTitle = document.getElementById("product-title");
  const productPrice = document.getElementById("product-price");
  const productDescription = document.getElementById("product-description");
  const featuredImageContainer = document.getElementById("featured-image-container");
  const featuredImage = document.getElementById("featured-image");
  const productAuthor = document.getElementById("product-author");
  const productStock = document.getElementById("product-stock");
  const addToCartBtn = document.getElementById("add-to-cart-btn");
  const cartCount = document.getElementById("cart-count");

  // --- FUNCTIONS ---
  function showState(state) {
    loadingState.classList.toggle("hidden", state !== "loading");
    errorState.classList.toggle("hidden", state !== "error");
    productContent.classList.toggle("hidden", state !== "ready");
  }

  function getCategoryLabel(categoryCode) {
    const categoryMapping = {
      FOOTWEAR: "Footwear",
      JERSEY: "Jersey",
      SHORTS: "Shorts",
    };
    return categoryMapping[categoryCode] || categoryCode;
  }

  function renderProduct(product) {
    document.title = `${product.name} - Adidaru Store`;
    productTitle.textContent = product.name;
    productPrice.textContent = `Rp${product.price.toLocaleString("id-ID")}`;
    productDescription.textContent = product.description;
    productAuthor.textContent = product.user_username || "Anonymous";
    productStock.textContent = product.stock;

    // Badges
    badgesContainer.innerHTML = "";
    const categoryBadge = document.createElement("span");
    categoryBadge.className =
      "inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-emerald-100 text-emerald-800";
    categoryBadge.textContent = getCategoryLabel(product.category);
    badgesContainer.appendChild(categoryBadge);

    if (product.is_featured) {
      const featuredBadge = document.createElement("span");
      featuredBadge.className =
        "inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800";
      featuredBadge.textContent = "Featured";
      badgesContainer.appendChild(featuredBadge);
    }

    // Image
    if (product.thumbnail) {
      featuredImage.src = product.thumbnail;
      featuredImage.alt = product.name;
      featuredImageContainer.classList.remove("hidden");
    } else {
      featuredImageContainer.classList.add("hidden");
    }

    // Add to Cart button
    if (product.stock > 0) {
      if (
        document.body.dataset.userId &&
        Number(document.body.dataset.userId) === Number(product.user_id)
      ) {
        addToCartBtn.disabled = true;
        addToCartBtn.textContent = "This is your product";
        addToCartBtn.classList.add("bg-gray-400", "cursor-not-allowed");
        addToCartBtn.classList.remove("bg-emerald-500", "hover:bg-emerald-600");
      } else {
        addToCartBtn.disabled = false;
      }
    } else {
      addToCartBtn.disabled = true;
      addToCartBtn.textContent = "Out of Stock";
      addToCartBtn.classList.add("bg-gray-400", "cursor-not-allowed");
      addToCartBtn.classList.remove("bg-emerald-500", "hover:bg-emerald-600");
    }
  }

  async function loadProductDetail() {
    try {
      showState("loading");
      const response = await fetch(PRODUCT_DETAIL_ENDPOINT);
      if (!response.ok) throw new Error("Failed to fetch product detail");
      const productData = await response.json();
      renderProduct(productData);
      showState("ready");
    } catch (error) {
      console.error("Error loading product detail:", error);
      showState("error");
    }
  }

  async function addToCart() {
    try {
      addToCartBtn.disabled = true;
      addToCartBtn.innerHTML = `<svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V4a4 4 0 00-4 4H4z"></path></svg> Adding...`;

      const response = await fetch(ADD_TO_CART_ENDPOINT, {
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
    } finally {
      addToCartBtn.disabled = false;
      addToCartBtn.innerHTML = `<i data-lucide="shopping-cart" class="w-6 h-6"></i> Add to Cart`;
      lucide.createIcons();
    }
  }

  // --- EVENT LISTENERS ---
  addToCartBtn.addEventListener("click", addToCart);

  // --- INITIALIZATION ---
  loadProductDetail();
  lucide.createIcons();
});
