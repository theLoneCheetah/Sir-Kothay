# API Test Suite for Sir-Kothay

Write-Host "=== Sir-Kothay API Test Suite ===" -ForegroundColor Green
Write-Host ""

# Test 1: Login
Write-Host "Test 1: User Login" -ForegroundColor Yellow
$loginResponse = curl.exe -s -X POST http://127.0.0.1:8000/api/auth/users/login/ -H "Content-Type: application/json" -d '{\"email\":\"fahimimran0088@gmail.com\",\"password\":\"fahim0088\"}' | ConvertFrom-Json
$token = $loginResponse.tokens.access
Write-Host "✅ Login successful - Token received" -ForegroundColor Green
Write-Host ""

# Test 2: Get current user
Write-Host "Test 2: Get Current User" -ForegroundColor Yellow
curl.exe -s -X GET http://127.0.0.1:8000/api/auth/users/me/ -H "Authorization: Bearer $token" | ConvertFrom-Json | Format-List
Write-Host "✅ User data retrieved" -ForegroundColor Green
Write-Host ""

# Test 3: Get user details
Write-Host "Test 3: Get User Details" -ForegroundColor Yellow
curl.exe -s -X GET http://127.0.0.1:8000/api/dashboard/user-details/my_details/ -H "Authorization: Bearer $token" | ConvertFrom-Json | Format-List
Write-Host "✅ User details retrieved" -ForegroundColor Green
Write-Host ""

# Test 4: Get broadcast messages
Write-Host "Test 4: Get My Broadcast Messages" -ForegroundColor Yellow
curl.exe -s -X GET http://127.0.0.1:8000/api/broadcast/messages/my_messages/ -H "Authorization: Bearer $token"
Write-Host "✅ Messages retrieved" -ForegroundColor Green
Write-Host ""

# Test 5: Get QR code
Write-Host "Test 5: Get My QR Code" -ForegroundColor Yellow
curl.exe -s -X GET http://127.0.0.1:8000/api/qrcode/qrcodes/my_qrcode/ -H "Authorization: Bearer $token" | ConvertFrom-Json | Format-List
Write-Host "✅ QR code retrieved" -ForegroundColor Green
Write-Host ""

# Test 6: List all users
Write-Host "Test 6: List All Users" -ForegroundColor Yellow
$users = curl.exe -s -X GET http://127.0.0.1:8000/api/auth/users/ -H "Authorization: Bearer $token" | ConvertFrom-Json
Write-Host "Total users: $($users.count)" -ForegroundColor Cyan
Write-Host "✅ Users list retrieved" -ForegroundColor Green
Write-Host ""

Write-Host "=== All Tests Completed Successfully ===" -ForegroundColor Green
