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

PROMO_CODE_STATUS_CHOICES = (
    ("Active", "Active"),
    ("No active", "No active"),
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

PAYMENT_METHOD_CHOICES = (
    ("Credit or Debit Card", "Credit or Debit Card"),
    ("Paypal", "Paypal"),
    ("Cash on Delivery (COD)", "Cash on Delivery (COD)"),
)
