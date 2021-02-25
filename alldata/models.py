from django.db import models

class User(models.Model):
    userid = models.AutoField(db_column='userid', primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45, blank=True, null=True)
    profile_photo = models.CharField(max_length=500)
    gender = models.CharField(max_length=45, choices=[('male', 'male'), ('female', 'female')])

    class Meta:
        db_table = 'User'
        unique_together = (('userid', 'first_name', 'last_name'),)

class BankCard(models.Model):
    bankcardid = models.AutoField(db_column='bankcardid', primary_key=True)
    user_userid = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_userid')
    name = models.CharField(max_length=45)
    valid_date = models.DateField()
    number = models.BigIntegerField()
    cvv = models.IntegerField()

    class Meta:
        db_table = 'BankCard'
        unique_together = (('bankcardid', 'name', 'user_userid'),)

class Location(models.Model):
    locationid = models.AutoField(db_column='locationid', primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=2000)

    class Meta:
        db_table = 'Location'
        unique_together = (('locationid', 'name'),)

class TripInstance(models.Model):
    tripinstanceid = models.AutoField(db_column='tripinstanceid', primary_key=True)
    price = models.IntegerField()
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=2000)

    class Meta:
        db_table = 'TripInstance'
        unique_together = (('tripinstanceid', 'title'),)

class Trip(models.Model):
    tripid = models.AutoField(db_column='tripid', primary_key=True)
    tripinstance_tripinstanceid = models.ForeignKey('TripInstance', on_delete=models.CASCADE, db_column='tripinstance_tripinstanceid')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    capacity = models.IntegerField()

    class Meta:
        db_table = 'Trip'
        unique_together = (('tripid', 'tripinstance_tripinstanceid'),)

class Guide(models.Model):
    guideid = models.AutoField(db_column='guideid', primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    description = models.CharField(max_length=2000)

    class Meta:
        db_table = 'Guide'
        unique_together = (('guideid', 'first_name', 'last_name'),)

class UserBuysTrip(models.Model):
    user_userid = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_userid')
    trip_tripid = models.ForeignKey('Trip', on_delete=models.CASCADE, db_column='trip_tripid')

    class Meta:
        db_table = 'UserBuysTrip'
        unique_together = (('user_userid', 'trip_tripid'),)

class LocationOfTripInstance(models.Model):
    location_locationid = models.ForeignKey('Location', on_delete=models.CASCADE, db_column='location_locationid')
    tripinstance_tripinstanceid = models.ForeignKey('TripInstance', on_delete=models.CASCADE, db_column='tripinstance_tripinstanceid')

    class Meta:
        db_table = 'LocationOfTripInstance'
        unique_together = (('location_locationid', 'tripinstance_tripinstanceid'),)

class GuideLeadsTrip(models.Model):
    user_userid = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_userid')
    trip_tripid = trip_tripid = models.ForeignKey('Trip', on_delete=models.CASCADE, db_column='trip_tripid')

    class Meta:
        db_table = 'GuideLeadsTrip'
        unique_together = (('user_userid', 'trip_tripid'),)

