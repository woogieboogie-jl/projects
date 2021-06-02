def get_boundaries(target, margin):
        low_limit = target - margin  
        high_limit = target + margin  
        return low_limit, high_limit


low, high = get_boundaries(150,50)
print("Low limit: " + str(low) + ", hight limit: " + str(high))