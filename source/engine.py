import winsound
import time
import os

class Engine:
    ''' Main engine '''
  
    buff, buff_title = '', 'Nothing, but a NoneType'

    def __init__(self, title, info, cur_colorama_obj):
        cur_colorama_obj.just_fix_windows_console()

        os.system(f'title {title}')

        self.greeting_beep()
        self.showinfo(title, info)

    def update(self, isaction=True):
        os.system('cls')

        lines = self.buff.split('\n')
        for line in lines:
            clean_line = self._strip_ansi(line)
            padding = max(0, (os.get_terminal_size().columns - len(clean_line)) // 2)
            print(' ' * padding + line)

        print()

        clean_title = self._strip_ansi(self.buff_title)
        padding = max(0, (os.get_terminal_size().columns - len(clean_title)) // 2 - 1)

        title_display = f'\033[38;2;5;207;2m{self.buff_title}\033[0;0m'

        if isaction:
            answer = input(f'{"=" * padding} {title_display} {"=" * padding}\n\n ? ')

            self.steps_beep()

            return answer

        else:
            print(f'{"=" * padding} {title_display} {"=" * padding}\n\n ', end='')
            os.system('pause')

            return

    def place(self, new_buff, title):
        self.buff = new_buff
        self.buff_title = title

    def showinfo(self, title, info):
        print(f'''
 \033[38;2;5;207;2mInstructions and info\033[0;0m for {title}: \033[38;2;255;0;0mREAD BEFORE PLAYING\033[0;0m

  1. Maximize your CMD window for better playing.
  2. Turn on your sound, if game provide sound effects/music.
  3. Use ONLY keyboard, because engine provides ONLY keyboard controls.

 -=- \033[38;2;5;207;2mINFO\033[0;0m -=-

{'\n'.join(f'  {line}' for line in info.split('\n'))}

''')

        os.system('pause')
        os.system('cls')
        self.greeting_beep()

    def greeting_beep(self):
        winsound.Beep(600, 100)
        winsound.Beep(800, 100)
        winsound.Beep(1000, 100)

    def steps_beep(self):
        winsound.Beep(275, 100)
        winsound.Beep(275, 100)
        winsound.Beep(275, 100)

    def _strip_ansi(self, text):
        """Removes ANSI"""
        import re
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def raiseerr(self, infoab):
        time.sleep(1)

        self.error_beep()

        os.system('cls')
        print(f' \033[38;2;255;0;0mAn unexpected error has occurred.\033[0;0m {infoab}\n')
        os.system('pause')

    def error_beep(self):
        winsound.Beep(450, 100)
        winsound.Beep(400, 800)

class Image:
    ''' Image-To-Text class. '''
  
    def __init__(self, path, pillow):
        self.pillow = pillow
        self.path = path

    def error_beep(self):
        winsound.Beep(450, 100)
        winsound.Beep(400, 800)

    def create(self):
        try:
            # Creating image
            terminal_width = os.get_terminal_size().columns
            terminal_height = os.get_terminal_size().lines - 4

            img = self.pillow.open(self.path)

            self.image = img.resize((terminal_width, terminal_height))
            self.symmap = []

            for y in range(self.image.height):
                line = []
                for x in range(self.image.width):
                    pixel = self.image.getpixel((x, y))
                    # Checking transparency of symbol
                    if len(pixel) == 4 and pixel[3] == 0:
                        line.append(' ') # Blank pixel
                    else:
                        line.append(f'\033[38;2;{pixel[0]};{pixel[1]};{pixel[2]}m▓\033[0;0m')

                self.symmap.append(''.join(line))

            return '\n'.join(self.symmap)

        except Exception as e:
            # Beeping on error
          
            time.sleep(1)
            self.error_beep()

            os.system('cls')
            print(f' \033[38;2;255;0;0mAn unexpected error has occurred.\033[0;0m {str(e.__class__.__name__)}: {str(e)}\n')
            os.system('pause')

class Sound:
    ''' Simple as a rock. '''
  
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        winsound.PlaySound(self.filename, winsound.SND_ASYNC | winsound.SND_FILENAME)

    def stop(self):
        winsound.PlaySound(None, 0)
