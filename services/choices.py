from datetime import datetime

now_date = int(datetime.now().strftime("%Y")) + 1


def year_choice():
    return ((year, year) for year in range(2011, now_date))


PRODUCT_STATUS_CHOICES = (
    ("Available Buy at Website", "Available Buy at Website"),
    ("Available Only at Cafe", "Available Only at Cafe")
)

SPACE_CHOICES = (
    ("Event Space", "Event Space"),
    ("Meeting Space", "Meeting Space"),
    ("Workspace", "Workspace")
)


EVENTS_STATUS_CHOICES = (
    ("Upcoming", "Upcoming"),
    ("Active", "Active"),
    ("Closed", "Closed")
)

RATING = (
    (1, '★✩✩✩✩'),
    (2, '★★✩✩✩'),
    (3, '★★★✩✩'),
    (4, '★★★★✩'),
    (5, '★★★★★'),
)

GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

PAYMENT_METHOD_CHOICES = (
    ("Credit or Debit Card", "Credit or Debit Card"),
    ("Paypal", "Paypal"),
    ("Cash on Delivery (COD)", "Cash on Delivery (COD)"),
)

DISCOUNT_CHOICES = (
    (5, "5% off"),
    (10, "10% off"),
    (15, "15% off"),
    (20, "20% off"),
    (25, "25% off"),
    (30, "30% off"),
    (40, "40% off"),
    (50, "50% off"),
    (60, "60% off"),
    (70, "70% off"),
)


TRACK_ORDER_STATUS = (
    ("Parcel is successfully delivered", "Parcel is successfully delivered"),
    ("Parcel is out for delivery", "Parcel is out for delivery"),
    ("Parcel is received at delivery Branch", "Parcel is received at delivery Branch"),
    ("Parcel is in transit", "Parcel is in transit"),
    ("Sender has shipped your parcel", "Sender has shipped your parcel"),
    ("Sender is preparing to ship your order", "Sender is preparing to ship your order"),
)
