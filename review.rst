============================
Microservice: Review
============================

Đảm nhiệm các chức năng đầy đủ bao gồm: xem, tạo mới, sửa, xóa, tương ứng với các phương thức get(),post, put/path, delete


.. _review-001:

Phương thức GET
================================
URL của phương thức get

http://review.curama.jp/v1/{category}/{service_type}/?params


Yêu cầu chức năng :
--------------------
* Lấy về những dữ liệu phù hợp và chính xác với yêu cầu

Thông số
----------

:HTTP Method:
    GET

:Request Data Type:
    URL

:ViewClass:
    Unimplemented

:permission:
    Unimplemented

Request
-------------

.. list-table::

    * - name
      - type
      - data type
      - example
      - comment

    * - category
      - url params
      - string
      - aircon
      - tên một category

    * - service_type
      - url params
      - string
      - wall
      - tên một loại dịch vụ trong category (chú ý tham số này có khi có tham số category)

    * - store
      - query string
      - int
      - 1
      - id của 1 store có trong category và service_type (ý tưởng ban đầu tạo lên là tên shop, tuy nhiên tên shop có thể trùng nhau hoặc quá dài, nên tham số này thành ra query id của cửa hàng có tên gần giống nhau)

    * - service
      - query string
      - int
      - 1
      - query ra cái service nó muốn review. 

    * - star
      - query string
      - list[int]
      - [1,2,3]
      - tìm ra cái thằng service nào được đánh giá khoản 1,2,3 sao gì đấy

    * - sort
      - query string
      - string
      - latest-adddate
      - sắp xếp thoe thằng nào, ví dụ sắp sếp theo giá thành

    * - limit
      - query string
      - int
      - 10
      - cái này giống phân trang hơn. (éo biết cái này làm gì luôn :D)

    * - offset
      - query string
      - int
      - 11
      - lấy các bản ghi từ cái limit +1 sang trang tiếp theo

Request Sample

::

    # Hiển thị 10 reviews( mặc định là 10 revews mới nhất)
    http://review.curama.jp/v1/reviews/

    # hiển thị các review có trong category aircon, có đánh giá là 1,2 sao
    http://review.curama.jp/v1/reviews/aircon/?star=1,2

    # Hiển thị các reviews của store có id =1, không có service_type
    http://review.curama.jp/v1/reviews/?store=1

    # Hiển thị tất cả những review của thằng service đầu tiên. 
    http://review.curama.jp/v1/reviews/?service=1


Response
--------------

.. list-table::

    * - name
      - data type
      - example
      - comment

    * - review_id
      - int
      - 1
      - id của review

    * - reviewer
      - string
      - concáonhỏ
      - tên của người dùng viết bình luận

    * - service_category
      - string
      - aircon( điều hòa/máy lạnh)
      - Category của cais service

    * - service_type
      - string
      - loại thẳng đứng
      - tên loại dịch vụ

    * - use_date
      - string
      - 8/2015
      - ngày đã sử dụng dịch vu

    * - use_area
      - string
      - Hà Nội
      - khu vực đã đăng ký

    * - stars
      - float
      - 5.0
      - mức điểm đánh giá cho dịch vụ/ cửa hàng/ đối tượng được bình luận

    * - comment
      - string
      - HỌ sửa chữa/làm sạch cũng được, nhưng không ra gì
      - nội dung họ review

    * - link_to_review
      - string
      - http://curama.jp/review/1/
      - link dẫn đến cái review được hiển thị

    * - link_to_service
      - string
      - http://curama.jp/aircon/wall/1/
      - link dẫn đến cái dich vụ họ review


Response Sample

::

    {
        "links": {
            "count": 10,
            "nextlink": "http://review.curama.jp/v1/reviews/?limit=10&offset=11",
            "previsiouslink": null,
            "limit": 10,
            "offset": null
        },
        "results": {
            [
                {
                    "review_id": 1,
                    "reviewer": "テストのユーザ ,
                    "service_category": "エアコンクリーニング",
                    "service_type": "壁掛けタイプ",
                    "use_date": "2015年08月",
                    "use_area": "東京都渋谷区",
                    "stars": 5.0,
                    "comment": "口コミ口コミ口コミ",
                    "link_to_review": "http://curama.jp/review/1/",
                    "link_to_service": "http://curama.jp/aircon/wall/1/"
                },
                {
                    "review_id": 2,
                    "reviewer": "テストのユーザ ,
                    "service_category": "エアコンクリーニング",
                    "service_type": "壁掛けタイプ",
                    "use_date": "2015年08月",
                    "use_area": "東京都渋谷区",
                    "stars": 3.0,
                    "comment": "口コミ口コミ口コミ",
                    "link_to_review": "http://curama.jp/review/2/",
                    "link_to_service": "http://curama.jp/aircon/wall/1/",
                },
                ...
            ]
        }
    }

Bây giờ tao muốn phải đảm nhiệm được những request như sau:
-----------------------------------------------------------
- Tao muốn có thể hiển thị danh sách những review mới nhất trong 1 category , trong 1 category_type, 1 store, 1 service

  :: url: http://curama.jp/{category}/{service_type}/{store_id}/{service_id}/reviews/?params

Giải thích các tham sô:
-------------------------
.. list-table::


  * - tên tham số
    - kiểu dữ liệu
    - ví dụ
    - ý nghĩa của tham số
    - required-field

  * - category
    - String
    - clean
    - tên 1 category
    - None

  * - service_type
    - String
    - clean_window
    - tên 1 loại  service trong category
    - phải có tên của category trước

  * - store_id
    - Integer
    - 1
    - id của store
    - None

  * - service_id
    - Integer
    - 1
    - Id của service
    - None

Những param có thể có:
-----------------------
  - star : chỉ số đánh giá mà review cung cấp
  - review_type :  loai danh gia

Các URL có thể có:
-------------------
   - Hiển thị 10 reviews mới nhất của category dọn vệ sinh
       http:// curama.jp/clean/reviews
   - Hiển thị 10 reviews mới nhất của category dọn vệ sinh, loại làm sạch cửa sổ
        http:// curama.jp/clean/cleanwindow/reviews
   - Hiển thị 10 review mới nhất của store kity có id = 1
       http:// curama.jp/clean/cleanwindow/store=1/reviews
   - Hiển thị 10 review mới nhất của service lau kính của cửa hàng kity
       http://curama.jp/clean/cleanwindow/store=1/service=1/reviews
   - Hiển thị những review của service lau kinhs của cửa hàng kity có đánh giá star 1,2
       http://curama.jp/clean/cleanwindow/store=1/service=1/reviews/star=[1,2] 
   - Hiển thị những review của store kity có star = 1,2 
       http:// curama.jp/clean/cleanwindow/store=1/reviews/star=[1,2]
   - Hiển thị những review của category clean có star = 1,2
       http://curama.jp/clean/reviews/star=1,2
   - Hiển thị những review của category clean có review_type=abc 
       http://curama.jp/clean/reviews/review_type=abc

Response:
---------
Khi trả về 1 review, phải trả về được những thông tin như sau:
  - id của review
  - tác giả của review(có thể là nickname của review)
  - điểm đánh giá của review
  - Nội dung review
  - review_type
  - link dẫn đến review 

Đối với review 1 dịch vụ (service) thì cần trả về(thêm):
  - ngày sử dụng dịch vụ (use_date)
  - nơi sử dụng dịch vụ (area :ví dụ Hà Nội)

Đối với những trường hợp thông qua thì phải trả về những thông tin trước đó cần thiết.

ví dụ trả về(theo các url được sắp xếp ở trên):
------------------------------------------------
  - ví dụ response trả về khi muốn lấy 10(ở đây chỉ có 3) review mới nhất của các service có trong category

"results":{
    "category":
          { name:"clean",
            descrtiption: "this ís description"}

    "reviews":
 
       [ {
          id: 1,

          review_type: "this example1"

          author: "concao",

          text: "no comments",

          star: 5

          area: HaNoi

          link: http://curama.jp/clean/cleanwindow/kity/cleana/reviews/1

         },
 
        {
          id: 109,

          review_type: "this example12",

          author: "concao111",

          text: "this is comments ",

          star: 2.0
          
          area: HaNoi

          link: http://curama.jp/clean/cleantable/jean/cleansr/reviews/109

        },

        {
          id: 100,

          review_type: "this example1",

          author: "concao111",

          text: "this is comments ",

          star: 5
  
          area: HaNoi

          http://curama.jp/clean/cleantable/tom/cleanb/reviews/100

         }

        ]

}





