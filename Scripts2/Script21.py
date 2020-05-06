'''Faça um programa em python que abra e reproduza um áudio de mp3.'''
import pygame
pygame.init()
pygame.mixer.music.load('faixa4.mp3')
pygame.mixer.music.play()
pygame.event.wait()