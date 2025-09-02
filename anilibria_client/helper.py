import m3u8_To_MP4

from ffmpeg.asyncio import FFmpeg

async def async_download(url: str, output_path: str):
    """
    Позволяет скачивать серию через URL (https://cache-rfn.libria.fun/videos/media/)
    ffmpeg required

    Args:
        url: Ссылка
        output_path: Дириктория
    """
    return await m3u8_To_MP4.async_download(m3u8_uri=url, mp4_file_dir=output_path)

async def async_ffmpeg_download(url: str, output_path: str) -> bool:
    """
    Скачивание m3u8 через ffmpeg с обходом блокировок (при блокировки основного метода async_download)

    !!!SLOW!!!
    
    Args:
        url: Ссылка
        output_path: Путь для сохранения MP4 файла
    """
    try:
        ffmpeg = (
            FFmpeg()
                .input(url)
                .output(output_path, **{"c": "copy", "bsf:a": "aac_adtstoasc"})
        )
        await ffmpeg.execute()
        return True
        
    except KeyError:
            return "Запрашиваемое видео недоступно."
    except ValueError:
        return "Неверная ссылка."
    except Exception as e:
        return "Произошла непредвиденная ошибка при загрузке видео: " + str(e)
