from sports.notifications.notification_center import (
    NotificationCenter,
)

from sports.notifications.models import (
    Notification,
)

from sports.notifications.models import (
    NotificationType,
)

center = NotificationCenter()


def printer(notification):

    print()

    print(notification.title)

    print(notification.message)


center.subscribe(printer)

notification = Notification(
    notification_type=NotificationType.GOAL,
    title="⚽ GOAL",
    message="Manchester City 2-1 Arsenal",
    fixture_id=1,
)

center.publish(notification)