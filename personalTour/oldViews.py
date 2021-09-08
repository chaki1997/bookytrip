'''
def archive_accommodation(request):

    print(request.session['cities'])
    city = request.session['cities'][0]['title']
    print(city)
    #orders = HotelOrder.objects.all()
    city = City.objects.get(city__exact=city)
    data_list = request.session['cities']
    cntx_city_list = []
    for i in data_list:
        cntx_city_list.append(i['title'])

    print(city)
    print(cntx_city_list)
    accommodations = Accommodation.objects.filter(city=city)
    print(accommodations)




    context = {
        'accommodations': accommodations,
        'cities': cntx_city_list
    }

    return render(request, 'personalTour/archive_accommodation.html', context)
'''