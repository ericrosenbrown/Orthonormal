blues = ring(:A3,:A3,:D3,:D3,:A3,:A3,:D3,:D3,:A3,:E3,:D3,:D3)
blues2 = ring(:A3,:D3,:A3,:D3,:A3,:A3,:D3,:D3,:A3,:E3,:D3,:D3,:A3)

define :bl2 do
  use_synth :fm
  2.times do
    4.times do
      play chord(:A3,:minor)
      sleep 1
    end
    4.times do
      play chord(:D3,:minor)
      sleep 1
    end
  end
  play chord(:A3,:minor)
  sleep 1
  play chord(:E3,:minor)
  sleep 1
  4.times do
    play chord(:D3,:minor)
    sleep 1
  end
end

define :bl3 do
  use_synth :fm
  2.times do
    8.times do
      play chord(:A3,:minor)
      sleep 0.5
    end
    8.times do
      play chord(:D3,:minor)
      sleep 0.5
    end
  end
  
  play chord(:A3,:minor)
  sleep 1
  play chord(:E3,:minor)
  sleep 1
  2.times do
    play chord(:D3,:minor)
    sleep 1
  end
end

define :drum do
  sample :bd_ada
  sleep 1
end

define :highhat do
  sample :drum_cymbal_closed
  sleep 0.5
end


define :snare do
  sleep 1
  sample :sn_dub
  sleep 1
end

define :buyem do
  2.times do
    4.times do
      sample :elec_wood
      sleep 1
    end
    8.times do
      sample :elec_wood
      sleep 0.5
    end
  end
end


define :happy do
  use_synth :pretty_bell
  2.times do
    play blues2.tick
    sleep 2
  end
  2.times do
    play blues2.tick
    sleep 0.25
  end
  2.times do
    play blues2.tick
    sleep 2
  end
  2.times do
    play blues2.tick
    sleep 0.25
  end
  2.times do
    play blues2.tick
    sleep 2
  end
  3.times do
    play blues2.tick
    sleep 0.25
  end
  sleep(6.25)
end

define :happy2 do
  use_synth :dtri
  3.times do
    play :A3
    sleep 2
    play :D3
    sleep 2
  end
  play :A3
  sleep 2
  play :D3
end


#Song starts below

#First instrument added
bl3

#Percussions added

1.times do
  in_thread do
    bl3
  end
  
  in_thread do
    16.times do
      drum
    end
  end
  
  in_thread do
    32.times do
      highhat
    end
  end
  
  in_thread do
    8.times do
      snare
    end
  end
end

sleep(20)

#add in happy

1.times do
  in_thread do
    bl3
  end
  
  in_thread do
    16.times do
      drum
    end
  end
  
  in_thread do
    32.times do
      highhat
    end
  end
  
  in_thread do
    8.times do
      snare
    end
  end
  
  in_thread do
    happy
  end
  sleep(20)
end

#add in more happy

2.times do
  in_thread do
    bl3
  end
  
  in_thread do
    16.times do
      drum
    end
  end
  
  in_thread do
    32.times do
      highhat
    end
  end
  
  in_thread do
    8.times do
      snare
    end
  end
  
  in_thread do
    happy
  end
  
  in_thread do
    happy2
  end
  
  in_thread do
    buyem
  end
  
  sleep(20)
end

#take out extra happy

1.times do
  in_thread do
    bl3
  end
  
  in_thread do
    16.times do
      drum
    end
  end
  
  in_thread do
    32.times do
      highhat
    end
  end
  
  in_thread do
    8.times do
      snare
    end
  end
  
  in_thread do
    happy
  end
  sleep(20)
end

#take out happy

1.times do
  in_thread do
    bl3
  end
  
  in_thread do
    16.times do
      drum
    end
  end
  
  in_thread do
    32.times do
      highhat
    end
  end
  
  in_thread do
    8.times do
      snare
    end
  end
end

sleep(20)

#take out percussions
bl3

