def pow(exponent):
    def power_function(base):
        return base ** exponent
    return power_function

square= pow(2);
cube= pow(3);

print(cube(4))