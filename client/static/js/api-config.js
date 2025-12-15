// API Configuration
// Update this URL to your deployed backend API URL
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://127.0.0.1:8000'
    : 'https://your-backend-api.com'; // Change this to your VPS backend URL

// API Endpoints
const API_ENDPOINTS = {
    // Auth endpoints
    LOGIN: `${API_BASE_URL}/api/auth/users/login/`,
    REGISTER: `${API_BASE_URL}/api/auth/users/register/`,
    CURRENT_USER: `${API_BASE_URL}/api/auth/users/me/`,
    CHANGE_PASSWORD: `${API_BASE_URL}/api/auth/users/change_password/`,
    
    // Dashboard endpoints
    USER_DETAILS: `${API_BASE_URL}/api/dashboard/user-details/my_details/`,
    UPDATE_USER_DETAILS: `${API_BASE_URL}/api/dashboard/user-details/update_my_details/`,
    
    // QR Code endpoints
    MY_QRCODE: `${API_BASE_URL}/api/qrcode/qrcodes/my_qrcode/`,
    GENERATE_QR: `${API_BASE_URL}/api/qrcode/qrcodes/generate/`,
    
    // Broadcast endpoints
    MESSAGES: `${API_BASE_URL}/api/broadcast/messages/my_messages/`,
    ACTIVE_MESSAGE: `${API_BASE_URL}/api/broadcast/messages/active_message/`,
    CREATE_MESSAGE: `${API_BASE_URL}/api/broadcast/messages/`,
};

// Helper function to get auth token from localStorage
function getAuthToken() {
    return localStorage.getItem('access_token');
}

// Helper function to make authenticated API requests
async function apiRequest(url, options = {}) {
    const token = getAuthToken();
    
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json',
            ...(token && { 'Authorization': `Bearer ${token}` }),
        },
    };
    
    const mergedOptions = {
        ...defaultOptions,
        ...options,
        headers: {
            ...defaultOptions.headers,
            ...options.headers,
        },
    };
    
    try {
        const response = await fetch(url, mergedOptions);
        return response;
    } catch (error) {
        console.error('API request failed:', error);
        throw error;
    }
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { API_BASE_URL, API_ENDPOINTS, getAuthToken, apiRequest };
}
