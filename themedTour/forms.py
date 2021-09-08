from django import forms
from .models import ThemedPackReview, OrderedThemedPack


class ThemedReviewForm(forms.ModelForm):
    class Meta:
        model = ThemedPackReview
        fields = ('comment',)

        comment = forms.CharField(
                error_messages={
               'required': 'Please enter your TRAKI'
                })

        # def check_comment(self):
        #     commet = self.cleaned_data.get("comment")
        #     if comment=="":
        #         return forms.ValidationError("this is pizdec") 


class OrderedThemedPackForm(forms.ModelForm):
    class Meta:
        model = OrderedThemedPack
        fields = ('order_start_date', 'order_end_date', 'order_travelers')