class GangwondoPackage:
    def __init__(self):
        self.places = ['강릉 경포해수욕장', '속초 바다정원카페']

    def __str__(self):
        return str(self.places)

if __name__ == '__main__':
    gp = GangwondoPackage()
    print(gp)