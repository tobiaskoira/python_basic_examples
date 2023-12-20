try:
    import glob
    print(glob.glob("C:/*"))
except ImportError:
    print("Tapahtui joku virhe")
