#!/usr/bin/env ruby
#Copyright DSK 2013

class Array
  def split_to_h(del)
    h = Hash[self.map {|k| k.split(del)}]
  end
end

# test code
# ar = ['item1: val1','item2: val2','item3: val3','item4: val4']
# puts ar.split_to_h(': ')
