# Sir-Kothay REST API Documentation

## Base URL
```
http://127.0.0.1:8000/api/
```

## Authentication
All authenticated endpoints require a JWT Bearer token in the Authorization header:
```
Authorization: Bearer <access_token>
```

---

## Authentication Endpoints

### 1. Register New User
**POST** `/api/auth/users/register/`

**Request Body:**
```json
{
  "email": "user@example.com",
  "username": "username",
  "password": "password123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Response:**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "first_name": "John",
    "last_name": "Doe",
    "is_active": true,
    "date_joined": "2025-12-15T21:00:00Z"
  },
  "tokens": {
    "refresh": "refresh_token_here",
    "access": "access_token_here"
  }
}
```

**cURL Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","username":"username","password":"password123"}'
```

---

### 2. Login
**POST** `/api/auth/users/login/`

**Request Body:**
```json
{
  "email": "fahimimran0088@gmail.com",
  "password": "fahim0088"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "user": {
    "id": 2,
    "email": "fahimimran0088@gmail.com",
    "username": "MD_IRFAN_HASAN_FAHIM",
    "first_name": "",
    "last_name": "",
    "is_active": true,
    "date_joined": "2025-11-16T20:54:57.521112Z"
  },
  "tokens": {
    "refresh": "refresh_token_here",
    "access": "access_token_here"
  }
}
```

**cURL Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"fahimimran0088@gmail.com","password":"fahim0088"}'
```

---

### 3. Get Current User
**GET** `/api/auth/users/me/`

**Headers:** 
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "id": 2,
  "email": "fahimimran0088@gmail.com",
  "username": "MD_IRFAN_HASAN_FAHIM",
  "first_name": "",
  "last_name": "",
  "is_active": true,
  "date_joined": "2025-11-16T20:54:57.521112Z"
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/auth/users/me/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 4. Change Password
**POST** `/api/auth/users/change_password/`

**Headers:**
- Authorization: Bearer {access_token}

**Request Body:**
```json
{
  "old_password": "fahim0088",
  "new_password": "newpassword123"
}
```

**Response:**
```json
{
  "message": "Password changed successfully"
}
```

**cURL Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/users/change_password/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"old_password":"fahim0088","new_password":"newpassword123"}'
```

---

### 5. List All Users (Admin/Staff Only)
**GET** `/api/auth/users/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "email": "user1@example.com",
      "username": "user1",
      "first_name": "",
      "last_name": "",
      "is_active": true,
      "date_joined": "2025-11-16T18:29:00.230272Z"
    }
  ]
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/auth/users/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## User Details Endpoints

### 6. Get My Details
**GET** `/api/dashboard/user-details/my_details/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "id": 2,
  "user": 2,
  "user_email": "fahimimran0088@gmail.com",
  "user_username": "MD_IRFAN_HASAN_FAHIM",
  "profile_image": "/media/profile_images/MD_IRFAN_HASAN_FAHIM_300_x_300_px.jpg",
  "profile_image_url": "/media/profile_images/MD_IRFAN_HASAN_FAHIM_300_x_300_px.jpg",
  "phone_number": "+8801580356046",
  "bio": "Product-focused developer...",
  "designation": "Senior Software Engineer",
  "organization": "Tech Company",
  "slug": "MD_IRFAN_HASAN_FAHIM-None"
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/dashboard/user-details/my_details/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 7. Update My Details
**PATCH** `/api/dashboard/user-details/update_my_details/`

**Headers:**
- Authorization: Bearer {access_token}

**Request Body:**
```json
{
  "phone_number": "+8801580356046",
  "bio": "Updated bio via API",
  "designation": "Senior Software Engineer",
  "organization": "Tech Company"
}
```

**Response:**
```json
{
  "id": 2,
  "user": 2,
  "user_email": "fahimimran0088@gmail.com",
  "user_username": "MD_IRFAN_HASAN_FAHIM",
  "profile_image": "/media/profile_images/MD_IRFAN_HASAN_FAHIM_300_x_300_px.jpg",
  "profile_image_url": "/media/profile_images/MD_IRFAN_HASAN_FAHIM_300_x_300_px.jpg",
  "phone_number": "+8801580356046",
  "bio": "Updated bio via API",
  "designation": "Senior Software Engineer",
  "organization": "Tech Company",
  "slug": "MD_IRFAN_HASAN_FAHIM-None"
}
```

**cURL Example:**
```bash
curl -X PATCH http://127.0.0.1:8000/api/dashboard/user-details/update_my_details/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"phone_number":"+8801580356046","bio":"Updated bio","designation":"Senior Engineer","organization":"Company"}'
```

---

### 8. List All User Details (Paginated)
**GET** `/api/dashboard/user-details/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [...]
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/dashboard/user-details/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Broadcast Message Endpoints

### 9. List My Messages
**GET** `/api/broadcast/messages/my_messages/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
[
  {
    "id": 4,
    "user": 2,
    "user_email": "fahimimran0088@gmail.com",
    "user_username": "MD_IRFAN_HASAN_FAHIM",
    "message": "This is a test message from API",
    "active": true
  }
]
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/broadcast/messages/my_messages/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 10. Get Active Message
**GET** `/api/broadcast/messages/active_message/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "id": 4,
  "user": 2,
  "user_email": "fahimimran0088@gmail.com",
  "user_username": "MD_IRFAN_HASAN_FAHIM",
  "message": "This is a test message from API",
  "active": true
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/broadcast/messages/active_message/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 11. Create Broadcast Message
**POST** `/api/broadcast/messages/`

**Headers:**
- Authorization: Bearer {access_token}

**Request Body:**
```json
{
  "message": "This is a test message from API",
  "active": true
}
```

**Response:**
```json
{
  "id": 4,
  "user": 2,
  "user_email": "fahimimran0088@gmail.com",
  "user_username": "MD_IRFAN_HASAN_FAHIM",
  "message": "This is a test message from API",
  "active": true
}
```

**cURL Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/broadcast/messages/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message":"Test message","active":true}'
```

---

### 12. List All Messages (Paginated)
**GET** `/api/broadcast/messages/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [...]
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/broadcast/messages/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 13. Set Message as Active
**POST** `/api/broadcast/messages/{id}/set_active/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "message": "Message set as active"
}
```

**cURL Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/broadcast/messages/4/set_active/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 14. Update Message
**PATCH** `/api/broadcast/messages/{id}/`

**Headers:**
- Authorization: Bearer {access_token}

**Request Body:**
```json
{
  "message": "Updated message",
  "active": false
}
```

**cURL Example:**
```bash
curl -X PATCH http://127.0.0.1:8000/api/broadcast/messages/4/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"message":"Updated message","active":false}'
```

---

### 15. Delete Message
**DELETE** `/api/broadcast/messages/{id}/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:** 204 No Content

**cURL Example:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/broadcast/messages/4/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## QR Code Endpoints

### 16. Get My QR Code
**GET** `/api/qrcode/qrcodes/my_qrcode/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "id": 2,
  "user": 2,
  "user_email": "fahimimran0088@gmail.com",
  "user_username": "MD_IRFAN_HASAN_FAHIM",
  "image": "/media/qr_codes/qr_2_MD_IRFAN_HASAN_FAHIM.png",
  "qr_url": "/media/qr_codes/qr_2_MD_IRFAN_HASAN_FAHIM.png",
  "generated_at": "2025-11-16T20:59:21.106407Z"
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/qrcode/qrcodes/my_qrcode/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 17. Generate QR Code
**POST** `/api/qrcode/qrcodes/generate/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "message": "QR code generated successfully",
  "qr_code": {
    "id": 2,
    "user": 2,
    "user_email": "fahimimran0088@gmail.com",
    "user_username": "MD_IRFAN_HASAN_FAHIM",
    "image": "/media/qr_codes/qr_2_MD_IRFAN_HASAN_FAHIM.png",
    "qr_url": "/media/qr_codes/qr_2_MD_IRFAN_HASAN_FAHIM.png",
    "generated_at": "2025-11-16T20:59:21.106407Z"
  }
}
```

**cURL Example:**
```bash
curl -X POST http://127.0.0.1:8000/api/qrcode/qrcodes/generate/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

### 18. List All QR Codes (Paginated)
**GET** `/api/qrcode/qrcodes/`

**Headers:**
- Authorization: Bearer {access_token}

**Response:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [...]
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/api/qrcode/qrcodes/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Testing Summary

All APIs have been successfully tested with the credentials:
- **Email:** fahimimran0088@gmail.com
- **Password:** fahim0088

### Test Results:
✅ User Login - Success  
✅ Get Current User - Success  
✅ Get User Details - Success  
✅ Update User Details - Success  
✅ Get Broadcast Messages - Success  
✅ Create Broadcast Message - Success  
✅ Generate QR Code - Success  
✅ Get QR Code - Success  
✅ Change Password - Success  
✅ List Users - Success  

---

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```
or
```json
{
  "error": "Invalid credentials"
}
```

### 403 Forbidden
```json
{
  "error": "Permission denied"
}
```

### 404 Not Found
```json
{
  "error": "User details not found"
}
```

### 400 Bad Request
```json
{
  "field_name": ["Error message"]
}
```

---

## Pagination

All list endpoints support pagination with the following query parameters:
- `page`: Page number (default: 1)
- `page_size`: Number of items per page (default: 10, max: 100)

Example:
```bash
curl -X GET "http://127.0.0.1:8000/api/broadcast/messages/?page=1&page_size=20" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Notes

1. All timestamps are in UTC format (ISO 8601)
2. JWT tokens expire after 5 hours (configurable in settings)
3. Refresh tokens can be used to obtain new access tokens
4. Media files (images, QR codes) are served from `/media/` URL
5. File uploads should use `multipart/form-data` content type
6. Default pagination is 10 items per page

---

## Quick Start Testing Script

```bash
# 1. Login and save token
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/api/auth/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"fahimimran0088@gmail.com","password":"fahim0088"}' \
  | jq -r '.tokens.access')

# 2. Get current user
curl -X GET http://127.0.0.1:8000/api/auth/users/me/ \
  -H "Authorization: Bearer $TOKEN"

# 3. Get user details
curl -X GET http://127.0.0.1:8000/api/dashboard/user-details/my_details/ \
  -H "Authorization: Bearer $TOKEN"

# 4. Get messages
curl -X GET http://127.0.0.1:8000/api/broadcast/messages/my_messages/ \
  -H "Authorization: Bearer $TOKEN"

# 5. Generate QR Code
curl -X POST http://127.0.0.1:8000/api/qrcode/qrcodes/generate/ \
  -H "Authorization: Bearer $TOKEN"
```
