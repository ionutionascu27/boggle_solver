from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    '''
    make a grid that will hold all the tiles for a boggle game
    '''
    return {(row , col): choice(ascii_uppercase) for row in range(height) for col in range(width)}
    
def get_neighbors(coords):
    '''
    get the neighbors for given coordinates
    '''
    
    # assign each coordinates component
    
    row = coords[0]
    col = coords[1]
    
    # enumerate all the possible neighbors
    
    top_left = (row-1, col-1)
    top = (row-1, col)
    top_right = (row-1, col+1)
    left = (row, col-1)
    right = (row, col+1)
    bot_left = (row+1,col-1)
    bot = (row+1, col)
    bot_right = (row+1, col+1)
    
    return [top_left, top, top_right, left, right, bot_left, bot, bot_right]
    
def all_grid_neighbors(grid):
    
    neighbors = {}
    
    for position in grid:
        neighbors_position = get_neighbors(position)
        neighbors[position] = [p for p in neighbors_position if p in grid]
        
    return neighbors
    
def path_to_word(grid, path):
    '''
    return the letters from a grid path into a string
    '''
    return ''.join([grid[p] for p in path])
    
def search(grid, dictionary):
    
    """
    Search through the paths to locate words by matching
    strings to words in a dictionary
    """
    
    neighbors = all_grid_neighbors(grid)
    paths = []
    full_words, partial_words = dictionary
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word in full_words:
            paths.append(path)
        if word not in partial_words:
            return
        for next_pos in neighbors[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
                    
    for position in grid:
        do_search([position])
        
    words_list = []
    for path in paths:
        words_list.append(path_to_word(grid, path))
        
    return set(words_list)
    
def get_dictionary(file):
    
    """
    load the dictionary file
    """
    full_words, partial_words = set(), set()
    
    with open(file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for pword in range(1, len(word)):
                partial_words.add(word[:pword])
                
    return full_words, partial_words
        
def main():
    
    grid = make_grid(5, 5)
    dictionary = get_dictionary("words.txt")
    words = search(grid, dictionary)
    words_output = []
    for word in words:
        words_output.append(word)
    print(words_output)
    print("%s words found" % len(words)) 
    
if __name__ == "__main__":
    main()        