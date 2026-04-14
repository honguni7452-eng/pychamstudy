import uvicorn

def main():
    uvicorn.run(
        app = 'scr.app:app',
    reload=True
    )

if __name__ == '__main__':
    main()