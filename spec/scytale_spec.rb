require 'scytale'

describe Scytale do
  describe 'given a message of len 8 and a key of 3' do
    test 'it returns 3' do
      expect(Scytale.new('message', 3).encrypt).to eq('mssieege')
    end
  end
end
