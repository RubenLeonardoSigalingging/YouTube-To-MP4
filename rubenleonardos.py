#!/usr/bin/env python3


def pengunduh_youtube():
	import pytube
	from pytube import YouTube
	from os import system
	system("clear")


	link_video=input("Link Video YouTube: ")
	link_video=str(link_video)

	
	# BUAT FUNGSI MODULE PYTUBE
	unduh_video_saya=YouTube(link_video)


	# DAPATKAN JUDUL DARI VIDEO YOUTUBE YANG AKAN SAYA UNDUH.
	print(f"[!] Judul Video: {unduh_video_saya.title}")


	# DAPATKAN CAPTIONS VIDEO YOUTUBE SAYA, EAAAA
	print(f"[!] Deskripsi Video: {unduh_video_saya.description}")


	# DAPATKAN THUMBNAIL DARI VIDEO YOUTUBE SAYA.
	print(f"[!] Thumbnail Video: {unduh_video_saya.thumbnail_url}")


	# UNDUH VIDEO DENGAN KUALITAS TERBAIK.
	unduh_video_saya=unduh_video_saya.streams.get_highest_resolution()


	# UNDUH VIDEO SAYA
	unduh_video_saya.download()
pengunduh_youtube()