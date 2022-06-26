def run():
	import pygame as pg

	pg.init()
	pg.font.init()
	
	width , height = 600,400
	screen = pg.display.set_mode((width,height),pg.RESIZABLE)

	pg.display.set_icon(pg.image.load("images/logo.png"))
	pg.display.set_caption("Tic Tac Toe")

	base_font = pg.font.Font(None,32)

	clock = pg.time.Clock()
	fps = 30

	name1 = ""
	name2 = ""

	input_rect1 = pg.Rect((400,200),(140,32))
	input_rect2 = pg.Rect((200,200),(140,32))

	color_active = pg.Color("lightskyblue3")
	color_inactive = ("gray15")

	color1 = color_inactive
	color2 = color_inactive

	done = False
	active1 = False
	active2 = False

	while not done:
		screen.fill((255,255,255))
		clock.tick(fps)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True
			if event.type == pg.MOUSEBUTTONDOWN:
				if input_rect1.collidepoint(event.pos):
					active1 = True
				else:
					active1 = False
				if input_rect2.collidepoint(event.pos):
					active2 = True
				else:
					active2 = False
			if event.type == pg.KEYDOWN:
				if active1:
					if event.key == pg.K_BACKSPACE: name1 = name1[:-1]
					else:
						if not len(name1) == 15: name1 += event.unicode
				if active2:
					if event.key == pg.K_BACKSPACE: name2 = name2[:-1]
					else:
						if not len(name2) == 15: name2 += event.unicode
		if active1:
		    color1 = color_active
		else:
		    color1 = color_inactive
		if active2:
		    color2 = color_active
		else:
		    color2 = color_inactive

		pg.draw.rect(screen,color1,input_rect1,2)
		pg.draw.rect(screen,color2,input_rect2,2)

		text_surface1 = base_font.render(name1,True,(0,0,0))
		screen.blit(text_surface1,(input_rect1.x+5,input_rect1.y+5))

		text_surface2 = base_font.render(name2,True,(0,0,0))
		screen.blit(text_surface2,(input_rect2.x+5,input_rect2.y+5))

		pg.display.flip()

	pg.quit()
run()