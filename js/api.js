const API = {
  generateToken: async () => ({ token: Math.floor(Math.random() * 100) }),

  sendOTP: async (phone) => ({ success: true }),

  verifyOTP: async (phone, otp) => ({ success: true }),

  placeOrder: async (data) => ({
    orderId: "ORD" + Date.now(),
  }),

  getOrderStatus: async () => ({
    status: "QUEUE",
  }),

  getActiveOrders: async () => [],

  updateOrderStatus: async () => ({ success: true }),

  verifyDeliveryOTP: async () => ({ success: true }),

  getCompletedOrders: async () => [],

  getLogs: async () => [],
};
