from rest_framework import serializers
from catalog.models import BookInstance


class CatlogSerializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)
    book=serializers.CharField(required=True,max_length=100)
    imprint=serializers.CharField(required=True,max_length=100)
    due_back=serializers.DateField(required=False)
    borrower=serializers.CharField(required=False,allow_blank=True)

    LOAN_STATUS = (
		('d', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)
    status=serializers.ChoiceField(choices=LOAN_STATUS, default='a')



    def create(self,validated_data):

        return BookInstance.objects.create(**validated_data)


    def update(self, instance, validated_data):

        instance.book = validated_data.get('book',instance.book)    
        instance.imprint=validated_data.get('imprint',instance.imprint)    
        instance.due_back=validated_data.get('due_back',instance.due_back)    
        instance.borrower=validated_data.get('borrower',instance.borrower)    
        instance.status=validated_data.get('status',instance.status)    

        instance.save()
        return instance