from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from CodeRequester.models import User, RedeemCode, RedeemObject
from CodeRequester.forms import RequestForm, CodeVerifyForm

from utility import get_redeem_code


REDEEM_OBTAIN_LIMIT = 3

def request_code(request):

    if request.method == 'POST':  # Form is submitted
        form = RequestForm(request.POST)
        if form.is_valid():
            # Check if user is already existed
            try:
                user = User.objects.get(email=form.cleaned_data['email'])

                # Check if redeemed object is larger than limit
                if user.redeemed_objects.count() >= REDEEM_OBTAIN_LIMIT:
                    return render(request, 'CodeRequester/error_message.html', {'message': 'Exceed Redeem Limit'})

            except User.DoesNotExist:
                # Create new user info
                user = User(email=form.cleaned_data['email'])
                user.save()

            # Check if redeem code is already existed
            try:
                redeem_code = RedeemCode.objects.get(user=user)
            except RedeemCode.DoesNotExist:
                # Make sure the redeem code is unique,
                # Duplicated code will generate integrity error and regenerate new code
                redeem_code = RedeemCode(code=get_redeem_code(), user=user)
                while True:
                    try:
                        redeem_code.save()
                    except IntegrityError:
                        redeem_code.code = get_redeem_code()
                        pass
                    else:
                        break

            return render(request, 'CodeRequester/show_code.html', {'redeem_code': redeem_code})

    else:
        form = RequestForm()

    return render(request, 'CodeRequester/request_code.html', {'form': form})


def code_verify(request):

    if request.method == 'POST':  # Form is submitted
        form = CodeVerifyForm(request.POST)
        if form.is_valid():
            # Check if code is valid
            try:
                code = RedeemCode.objects.get(code=form.cleaned_data['code'])

                # Check if redeemed object is larger than limit
                if code.user.redeemed_objects.count() >= REDEEM_OBTAIN_LIMIT:
                    return render(request, 'CodeRequester/error_message.html', {'message': 'Exceed Redeem Limit'})

                redeem_object = RedeemObject.objects.order_by('?')[0]  # Get random object for user to redeem
                code.user.redeemed_objects.add(redeem_object)
                code.delete()
            except RedeemCode.DoesNotExist:
                return redirect('request')

            return render(request, 'CodeRequester/show_object.html', {'redeem_object': redeem_object})

    else:
        form = CodeVerifyForm()

    return render(request, 'CodeRequester/verify_code.html', {'form': form})