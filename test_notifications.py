from sports.notifications.notification_service import (
    NotificationService,
)

service = NotificationService()

service.send_system_message(
    "Notification Engine Online!"
)

service.goal(
    fixture_id=1,
    team="Manchester City",
    scorer="Erling Haaland",
    minute="84",
)