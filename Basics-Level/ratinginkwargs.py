

def salary(base=0, **kwargs):
    if 'rating' in kwargs and kwargs['rating'] == 'high':
        if 'hike' in kwargs:
            hike = kwargs['hike']
        else:
            hike = 0.1
        return round(base*(1+hike), 2)
    else:
        if 'hike' in kwargs:
            hike = kwargs['hike']
        else:
            hike = 0.05
        return round(base*(1+hike), 2)