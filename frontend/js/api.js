const BASE_URL = "http://127.0.0.1:8000";

const API = {

  // 🛒 CREATE ORDER
  placeOrder: async (data) => {
    let res = await fetch(`${BASE_URL}/orders`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    return res.json();
  },

  // 🔍 GET ORDER BY PHONE
  getUserOrder: async (phone) => {
    let res = await fetch(`${BASE_URL}/orders/phone/${phone}`);
    return res.json();
  },

  // 📦 GET ALL ORDERS (ADMIN / DISPLAY)
  getOrders: async () => {
    let res = await fetch(`${BASE_URL}/orders`);
    return res.json();
  },

  // 🔄 UPDATE STATUS (ADMIN)
  updateOrderStatus: async (orderId, status) => {
    let res = await fetch(`${BASE_URL}/orders/${orderId}/status`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status }),
    });

    return res.json();
  },

  // 🔐 VERIFY OTP
  verifyDeliveryOTP: async (orderId, otp) => {
    let res = await fetch(`${BASE_URL}/orders/${orderId}/verify-otp`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ otp }),
    });

    return res.json();
  }

};