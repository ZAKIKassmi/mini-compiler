
const AudioPlayer = ({audio}: {audio:string}) => {
  return (
    <div>
      <h3>Audio Player</h3>
      <audio controls>
        <source src={audio.replace("/public","")} type="audio/mpeg" />
        Your browser does not support the audio element.
      </audio>
    </div>
  );
};

export default AudioPlayer;