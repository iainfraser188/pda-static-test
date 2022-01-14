### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:                  # should have two "=" instead of one
      return True
    else                                #no ":" aftert else
      return False
   

  dif highest_card(self, card1 card2):  # called dif not def
  if card1.value > card2.value:          # no comma between card1 and card2
    return card                         #card should be called card1
  else:                                 # incorrrect indentation
    return card2
  


def cards_total(self, cards):
  total                                    # should have "=0"after total
  for card in cards:
    total += card.value
    return "You have a total of" + total   #incorrect indentation and total should be str(total)
  
```
