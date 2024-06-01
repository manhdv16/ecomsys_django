from djongo import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Room {self.room_number} on floor {self.floor}"

class Bed(models.Model):
    bed_number = models.CharField(max_length=10)
    room = models.ForeignKey(Room, related_name='beds', on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_number} in room {self.room.room_number}"
