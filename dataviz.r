library(av)
# load and normalize pcm data to match that of python file
df <- read.csv("data/divinity_audio_sample_data.csv")

plot(df$Time, df$Amplitude)