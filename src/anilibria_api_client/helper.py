import m3u8_To_MP4
import os # only for path / make dir
import aiofiles

from .api_client import AsyncAnilibriaAPI
from .exceptions import AnilibriaException

from ffmpeg.asyncio import FFmpeg

async def async_download(url: str, output_path: str = None, filename: str = "output.mp4"):
    """
    Позволяет скачивать серию через URL (https://cache-rfn.libria.fun/videos/media/)
    ffmpeg required

    Args:
        url: Ссылка на m3u8 плейлист
        output_path: Полный путь к выходному файлу (включая имя файла и расширение .mp4)
    """
    if output_path is None:
        mp4_file_dir = os.getcwd()
        mp4_file_name = filename
    else:
        mp4_file_dir = os.path.dirname(output_path)
        mp4_file_name = os.path.basename(output_path)

        if not mp4_file_dir:
            mp4_file_dir = os.getcwd()

    if not os.path.exists(mp4_file_dir):
        os.makedirs(mp4_file_dir, exist_ok=True)

    return m3u8_To_MP4.multithread_download(
        m3u8_uri=url,
        mp4_file_dir=mp4_file_dir,
        mp4_file_name=mp4_file_name
    )

async def async_ffmpeg_download(url: str, output_path: str) -> bool:
    """
    Скачивание m3u8 через ffmpeg с обходом блокировок (при блокировки основного метода async_download)

    Может быть медленным, используйте хороший интернет
    
    Args:
        url: Ссылка
        output_path: Путь для сохранения MP4 файла
    """
    try:
        ffmpeg = (
            FFmpeg()
                .input(url)
                .output(output_path, **{
                    "vcodec": "libx264",
                    "crf": 27,
                    "preset": "veryfast",
                    "c:a": "copy", 
                    "bsf:a": "aac_adtstoasc"
                    }
                )
        )
        await ffmpeg.execute()
        return True
        
    except KeyError:
            return "Запрашиваемое видео недоступно."
    except ValueError:
        return "Неверная ссылка."
    except Exception as e:
        return "Произошла непредвиденная ошибка при загрузке видео: " + str(e)

async def auth(api: AsyncAnilibriaAPI, login: str, password: str):
    try:
        res = await api.accounts.users_auth_login(login=login, password=password)

        return AsyncAnilibriaAPI(authorization=f"Bearer {res.get("token")}")
    except AnilibriaException as e:
        raise AnilibriaException("Auth error!")
    
async def download_torrent_file(torrent_bytes: bytes, filename: str):
    """
    Асинхронно сохраняет .torrent файл
    
    Args:
        torrent_bytes: бинарные данные torrent-файла
        filename: имя файла
    """
    if not filename.endswith('.torrent'):
        filename += '.torrent'
    
    async with aiofiles.open(filename, 'wb') as f:
        await f.write(torrent_bytes)
    
    return True 
