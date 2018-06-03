
import asyncio
import functools
import signal

from aiohttp.web import Application as Server
from aiohttp.web import run_app

from api import student_api, lector_api


def start_server(host, port):
    try:
        run_server(host, port)
    except Exception as e:
        print(e)
        return


def stop_server():
    asyncio.get_event_loop().stop()


def run_server(host, port, handle_signals=False):
    event_loop = asyncio.get_event_loop()
    event_loop.add_signal_handler(signal.SIGINT, functools.partial(stop_server))
    event_loop.add_signal_handler(signal.SIGTERM, functools.partial(stop_server))

    server = Server()
    init_handlers(server)
    run_app(server, host=host, port=port, handle_signals=handle_signals)


def init_handlers(server):

    server.router.add_post(
        "/student/auth",
        student_api.auth
    )

    server.router.add_post(
        "/student/students__info",
        student_api.get_info
    )

    server.router.add_post(
        "/student/current__pair",
        student_api.get_current_pair
    )

    server.router.add_post(
        "/student/send_qr",
        student_api.send_qr
    )

    server.router.add_post(
        "/lector/auth",
        lector_api.auth
    )

    server.router.add_post(
        "/lector/generate__qr",
        lector_api.generate_qr
    )

    server.router.add_post(
        "/lector/get__list",
        lector_api.get_students_list
    )

    server.router.add_static(
        "/static/",
        "./static"
    )

server_settings = {
    "host": "127.0.0.1",
    "port": 8080,
}

def main():
    start_server(
        **server_settings
)


if __name__ == "__main__":
    main()
