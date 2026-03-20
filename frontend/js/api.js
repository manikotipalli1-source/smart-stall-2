const API = {
  generateToken: async () => ({ token: Math.floor(Math.random() * 100) }),

  sendOTP: async (phone) => ({ success: true }),

  verifyOTP: async (phone, otp) => ({ success: true }),

  placeOrder: async (data) => {
    let orders = JSON.parse(localStorage.getItem("orders")) || [];

    let newOrder = {
      orderId: "ORD" + Date.now(),
      user: data.user || {},
      cart: data.cart || [],
      token: data.token || "",
      status: data.status || "QUEUE",
    };

    orders.push(newOrder);

    localStorage.setItem("orders", JSON.stringify(orders));

    return { orderId: newOrder.orderId };
  },

  getOrderStatus: async () => ({
    status: "QUEUE",
  }),

  getActiveOrders: async () => [],

  updateOrderStatus: async () => ({ success: true }),

  verifyDeliveryOTP: async () => ({ success: true }),

  getCompletedOrders: async () => [],

  getLogs: async () => [],

  getUserOrder: async (phone) => {
    let orders = JSON.parse(localStorage.getItem("orders")) || [];

    // ✅ SAFE FILTER (prevents crash)
    let userOrders = orders.filter(
      (order) => order.user && order.user.phone === phone,
    );

    if (userOrders.length === 0) return null;

    return userOrders[userOrders.length - 1];
  },
};
