import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  


	def __init__(self,):  
		"""Bloque sqrt"""
		gr.sync_block.__init__( 
		self,
		name='Sqrt',
		in_sig=[np.float32],
		out_sig=[np.float32]
		)
	

	def work(self, input_items, output_items):
		x=input_items[0]
		y=output_items[0]
		
		y[:]=np.sqrt(x)
		
		return len(x)

      
