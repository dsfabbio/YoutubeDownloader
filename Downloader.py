#!usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

cyanClaro = "\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro = '\033[1;35m'
amarelo = '\033[1;33m'

os.system('clear')
Banner = """
"""

Banner2 = """
▒▓▒▓▒▓▒▓▒▓▒▓─▄▀▀▀▄       +=================================================+
─██▀████▀██──▀▄▀──█      |     Download: Videos, Musicas e Playlists       |                                            
O▀████████▀O─────█       +=================================================+
───▀█▄▄█▀────────█       |      |
──▓▒▓▒▓▒▓▒───────█       | ☎ Criado por: Fabio Silva   |
                         | ☮ Data : 04.02.2018                             |
                         +=================================================+"""

Audio = """################
### USAGE ######
########################################################################################
################  Download Music | Videos and Playlist Music Videos  ###################
########################################################################################
###  Formatos disponiveis : mp3, mp4, flv, ogg, mkv, avi, webm                       ###
########################################################################################  
### Comands Options           |           FUNCTIONS                                  ###
########################################################################################
$$$ AUDIO $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
########################################################################################
###  -mp3                     >>> Download Faixa de Audio (Youtube)                  ###
###  --playlist-mp3           >>> Download de uma Playlist de Audio (Youtube)        ###
########################################################################################
###  -best                     >>> Download Faixa de Audio (Youtube)                 ###
###  --playlist-best           >>> Download de uma Playlist de Audio (Youtube)       ###
########################################################################################
###  -m4a                     >>> Download Faixa de Audio (Youtube)                  ###
###  --playlist-m4a           >>> Download de uma Playlist de Audio (Youtube)        ###
########################################################################################"""
Videos = """$$$ VIDEOS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
########################################################################################
###  -mp4                     >>> Download de video em formato MP4                   ###
###  --playlist-mp4           >>> Download de uma Playlist                           ###
########################################################################################
###  -flv                     >>> Download de video em formato flv                   ###
###  --playlist-flv           >>> Download de uma Playlist                           ###
########################################################################################
###  -ogg                     >>> Download de video em formato ogg                   ###
###  --playlist-ogg           >>> Download de uma Playlist                           ###
########################################################################################
###  -mkv                     >>> Download de video em formato mkv                   ###
###  --playlist-mkv           >>> Download de uma Playlist                           ###
########################################################################################
###  -avi                     >>> Download de video em formato avi                   ###
###  --playlist-avi           >>> Download de uma Playlist                           ###
########################################################################################
###  -webm                    >>> Download de video em formato webm                  ###
###  --playlist-webm          >>> Download de uma Playlist                           ###
########################################################################################
########################################################################################"""


def help():
    print (cyanClaro + Audio)
    print (amarelo + Videos)
    print(verde + 'Modo de uso:')
    print(verde + '$ python2 download.py [opções] [url]\n')
    print(verde + 'Example > python2 D0nwTube.py -mp3 https://www.youtube.com/watch?v=txmvb7tbAxs&t=57s')
    print(
    verde + 'Example > python2 D0nwTube.py playlist-mp3 https://www.youtube.com/playlist?list=PLQimmOQ9bzurCStHdAoBnZeRyzESSsc7q\n')
    print(verde + 'Example > python2 D0nwTube.py -mp4 https://www.youtube.com/watch?v=txmvb7tbAxs&t=57s')
    print(
    verde + 'Example > python2 D0nwTube.py playlist-mp4 https://www.youtube.com/playlist?list=PLQimmOQ9bzurCStHdAoBnZeRyzESSsc7q\n')
    print(' ')


print (vermelho + Banner)
print(verde + Banner2)


def main():
    try:
        if len(sys.argv) <= 3 and len(sys.argv) >= 2:
            opt = sys.argv[1]
            if opt == '-h' or opt == '--help':
                help()
            elif opt == '-mp3' or opt == '--audio':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                    quit()
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl -x --no-playlist --audio-format mp3 %s' % (url))
            elif opt == '--playlist-mp3':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    opt.system('youtube-dl -x --yes-playlist --audio-format mp3 %s' % (url))
                    ###########################################################################################################
                    #############################              Videos                                 #########################
                    ###########################################################################################################
            elif opt == '-mp4' or opt == '--video-mp4':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --no-playlist --recode-video mp4 %s' % (url))
            elif opt == '--playlist-mp3':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --yes-playlist --recode-video mp4 %s' % (url))

            elif opt == '-flv' or opt == '--video-flv':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --no-playlist --recode-video flv %s' % (url))
            elif opt == '--playlist-flv':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --yes-playlist --recode-video flv %s' % (url))

            elif opt == '-ogg' or opt == '--video-ogg':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --no-playlist --recode-video ogg %s' % (url))
            elif opt == '--playlist-ogg':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --yes-playlist --recode-video ogg %s' % (url))

            elif opt == '-webm' or opt == '--video-webm':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --no-playlist --recode-video webm %s' % (url))
            elif opt == '--playlist-webm':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --yes-playlist --recode-video webm %s' % (url))


            elif opt == '-mkv' or opt == '--video-mkv':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --no-playlist --recode-video mkv %s' % (url))
            elif opt == '--playlist-mkv':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --yes-playlist --recode-video mkv %s' % (url))

            elif opt == '-avi' or opt == '--video-avi':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --no-playlist --recode-video avi %s' % (url))
            elif opt == '--playlist-avi':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl --yes-playlist --recode-video avi %s' % (url))

                    #######################################################################################################
                    #######################################################################################################
            elif opt == '--playlist-mp4':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl -x --yes-playlist --recode-video mp4 %s' % (url))

            elif opt == '--playlist-flv':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl -x --yes-playlist --recode-video flv %s' % (url))

            elif opt == '--playlist-ogg':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl -x --yes-playlist --recode-video ogg %s' % (url))

            elif opt == '--playlist-webm':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl -x --yes-playlist --recode-video webm %s' % (url))

            elif opt == '--playlist-mkv':
                if len(sys.argv) <= 2:
                    print('Modo de uso\n')
                    print('$ python2 download.py [opção] [url]')
                else:
                    url = sys.argv[2]
                    os.system('youtube-dl -x --yes-playlist --recode-video mkv %s' % (url))


            else:
                print('Opção invalida, para ver o menu de ajuda use: \n')
                print('$ python2 download.py -h ou | python download.py --help')
        else:
            print('Você deve digitar alguma opção!\n')
            print('Modo de uso \n')
            print('$ python2 download.py [opção] [url]')
            print('$ python2 download.py -h, --help')
            quit()
    except KeyboardInterrupt:
        print('[!] 404 - Error Not Found;....[./]')


if __name__ == '__main__':
    main()