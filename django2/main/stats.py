import matplotlib as mp
from .models import xapi

def main():
    raw = xapi.onjects.all()
    print(type(raw))


if __name__ == '__main__':
    main()