require "sinatra"

def generate_progress()
    return rand().round(2)
end

def generate_activity_matrix()
    result = []
    (1..4).each do |w|
        daily = []
        (1..7).each do |d|
            daily.push rand(10)
        end
        result.push daily
    end
    return result
end

get '/user-statistics' do
      data = Hash.new
      data["name"] = "Marvin"
      data["id"] = 42
      data["registration"] = "2019-10-02"
      data["progress"] = generate_progress
      data["activity"] = generate_activity_matrix
      return data.to_json
end

# irb(main):002:0> generate_progress
# => 0.58
# irb(main):039:0> generate_activity_matrix
# => [[7, 7, 2, 8, 5, 7, 5], [9, 1, 7, 2, 4, 2, 0], [4, 4, 9, 1, 3, 2, 1], [5, 4, 1, 0, 5, 0, 4]]
