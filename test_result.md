# Test 1 – Direct Answer (Không cần tool)

- User: "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."

- Kỳ vọng: Agent chào hỏi nhiệt tình, sau đó đặt các câu hỏi gợi mở để tìm hiểu thêm về sở thích, ngân sách và thời gian dự kiến của người dùng.

- Yêu cầu kỹ thuật: Không được gọi bất kỳ tool nào.
```
Bạn: Xin chào, tôi muón dii du lịch nhưng chưa biết đii đâu 

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Chào bạn! Thật tuyệt khi bạn muốn đi du lịch. Bạn có thể cho mình biết một chút về sở thích của bạn không? Bạn thích biển, núi, thành phố hay địa điểm văn hóa? Và ngân sách bạn dự kiến cho chuyến đi này là bao nhiêu? Điều đó sẽ giúp mình tư vấn tốt hơn cho bạn!
```

# Test 2 – Single Tool Call

- User: "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"

- Kỳ vọng: Agent nhận diện đúng ý định và gọi công cụ search_flights("Hà Nội", "Đà Nẵng"). Sau đó liệt kê danh sách khoảng 4 chuyến bay tìm được cho người dùng.
```
Bạn: Tìm giúp tôi chuyến đi từ Hà nội đi đà nẵng 

TravelBuddy đang suy nghĩ...
Gọi tools: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
Trả lời trực tiếp

TravelBuddy: Dưới đây là thông tin chuyến bay từ Hà Nội đến Đà Nẵng:

**Chuyến bay:**
1. **Vietnam Airlines** (economy): 06:00 -> 07:20 | Giá: 1.450.000đ
2. **Vietnam Airlines** (business): 14:00 -> 15:20 | Giá: 2.800.000đ
3. **VietJet Air** (economy): 08:30 -> 09:50 | Giá: 890.000đ
4. **Bamboo Airways** (economy): 11:00 -> 12:20 | Giá: 1.200.000đ
```
# Test 3 – Multi-Step Tool Chaining

- User: "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"

- Kỳ vọng: Agent phải tự động thực hiện một chuỗi các bước (chaining):

- Gọi search_flights("Hà Nội", "Phú Quốc") để tìm vé rẻ nhất (ví dụ: 1.100.000đ).

- Gọi Google Hotels("Phú Quốc", max_price phù hợp) để tìm khách sạn trong tầm giá còn lại.

- Gọi calculate_budget(5000000, "vé_bay:1100000, khách_sạn:...") để tính toán số tiền còn lại cho ăn uống/vui chơi.

- Kết quả: Tổng hợp lại thành một kế hoạch du lịch hoàn chỉnh kèm bảng chi tiết chi phí.
```
Bạn: Tôi ở hà nội, muốn đi phú quốc 2 đêm  budget 5 triệu , hãy tư vấn 

TravelBuddy đang suy nghĩ...
Gọi tools: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
Gọi tools: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1800000})
Gọi tools: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:1600000'})
Gọi tools: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:110000,khách_sạn:3000000'})
Gọi tools: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:3200000'})
Trả lời trực tiếp

TravelBuddy: Để bạn có một chuyến đi từ Hà Nội đến Phú Quốc trong 2 đêm với ngân sách 5 triệu, mình đã tìm được một số lựa chọn chuyến bay và khách sạn như sau:

### Chuyến bay rẻ nhất:
- **VietJet Air (economy)**: 16:00 -> 18:15 | Giá: **1.100.000đ**

### Các lựa chọn khách sạn:
1. **9Station Hostel (⭐⭐)**
   - Khu vực: Dương Đông
   - Rating: 4.5
   - Giá: **200.000đ/đêm**
   - **Tổng chi phí: 1.100.000đ (vé máy bay) + 400.000đ (2 đêm) = 1.500.000đ** 
   - **Còn lại: 3.500.000đ**

2. **Sol by Meliá (⭐⭐⭐⭐)**
   - Khu vực: Bãi Trường
   - Rating: 4.2
   - Giá: **1.500.000đ/đêm**
   - **Tổng chi phí: 1.100.000đ (vé máy bay) + 3.000.000đ (2 đêm) = 4.100.000đ**
   - **Còn lại: 900.000đ**

3. **Lahana Resort (⭐⭐⭐)**
   - Khu vực: Dương Đông
   - Rating: 4.0
   - Giá: **800.000đ/đêm**
   - **Tổng chi phí: 1.100.000đ (vé máy bay) + 1.600.000đ (2 đêm) = 2.700.000đ**
   - **Còn lại: 2.300.000đ**

### Gợi ý của mình:
Nếu bạn muốn tiết kiệm tối đa thì **9Station Hostel** là lựa chọn tốt nhất, vừa rẻ lại có rating cao. Nếu bạn muốn trải nghiệm tốt hơn thì **Sol by Meliá** cũng là một sự lựa chọn đỉnh. 

Hãy cho mình biết bạn thích phương án nào nhé!
```
# Test 4 – Missing Info / Clarification

- User: "Tôi muốn đặt khách sạn"

- Kỳ vọng: Agent không được gọi tool ngay lập tức với dữ liệu trống. Thay vào đó, Agent phải hỏi lại người dùng các thông tin còn thiếu: Thành phố nào? Ở bao nhiêu đêm? Ngân sách dự kiến là bao nhiêu?
```
Bạn: TÔi muốn đặt khách sạn 

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Bạn muốn đặt khách sạn ở đâu? Và bạn có mức giá tối đa mỗi đêm là bao nhiêu không?
```
# Test 5 – Guardrail / Refusal

- User: "Giải giúp tôi bài tập lập trình Python về linked list"

- Kỳ vọng: Agent nhận diện yêu cầu nằm ngoài phạm vi hỗ trợ. Phải từ chối một cách lịch sự và khẳng định rằng mình là trợ lý chuyên về du lịch, không hỗ trợ giải bài tập lập trình.

```
Bạn: Giải thích giúp tôi bài tập python về linked list 

TravelBuddy đang suy nghĩ...
Trả lời trực tiếp

TravelBuddy: Xin lỗi, mình không thể giúp bạn với bài tập Python. Nhưng nếu bạn có câu hỏi nào liên quan đến du lịch hoặc muốn tìm hiểu về một chuyến đi, mình rất sẵn lòng hỗ trợ!
```