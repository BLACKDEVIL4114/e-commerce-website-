"""


"""
from django.contrib import admin
from django.urls import path, re_path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', views.logout_view,name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('admin-cancelled-returned', views.admin_cancelled_returned_view, name='admin-cancelled-returned'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('customer-forgot-password', views.customer_forgot_password_view, name='customer-forgot-password'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('my-order', views.my_order_view,name='my-order'),
    path('cancel-order/<int:pk>', views.cancel_order_view, name='cancel-order'),
    path('return-order/<int:pk>', views.return_order_view, name='return-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('buy-now/<int:pk>', views.buy_now_view,name='buy-now'),
    path('cart', views.cart_view,name='cart'),
    path('product-detail/<int:pk>', views.product_detail_view,name='product-detail'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('remove-all-from-cart/<int:pk>', views.remove_all_from_cart_view,name='remove-all-from-cart'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment', views.payment_view,name='payment'),
    path('payment-success', views.payment_success_view,name='payment-success'),

    # Wishlist
    path('wishlist', views.wishlist_view, name='wishlist'),
    path('add-to-wishlist/<int:pk>', views.add_to_wishlist_view, name='add-to-wishlist'),
    path('remove-from-wishlist/<int:pk>', views.remove_from_wishlist_view, name='remove-from-wishlist'),

    # Reviews
    path('submit-review/<int:pk>', views.submit_review_view, name='submit-review'),

    # Reorder
    path('reorder/<int:pk>', views.reorder_view, name='reorder'),

    # Coupons
    path('apply-coupon', views.apply_coupon_view, name='apply-coupon'),
    path('admin-coupons', views.admin_coupon_list_view, name='admin-coupons'),
    path('admin-add-coupon', views.admin_add_coupon_view, name='admin-add-coupon'),
    path('admin-delete-coupon/<int:pk>', views.admin_delete_coupon_view, name='admin-delete-coupon'),
    path('admin-toggle-coupon/<int:pk>', views.admin_toggle_coupon_view, name='admin-toggle-coupon'),

    # Sales Report
    path('admin-sales-report', views.admin_sales_report_view, name='admin-sales-report'),

    # Bulk Update & Export CSV
    path('admin-bulk-update-status/', views.admin_bulk_update_status_view, name='admin-bulk-update-status'),
    path('export-orders-csv', views.export_orders_csv_view, name='export-orders-csv'),

    # Complaints
    path('submit-complaint', views.submit_complaint_view, name='submit-complaint'),
    path('my-complaints', views.my_complaints_view, name='my-complaints'),
    path('admin-complaints', views.admin_view_complaints_view, name='admin-complaints'),
    path('update-complaint-status/<int:pk>', views.update_complaint_status_view, name='update-complaint-status'),

]

urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]


