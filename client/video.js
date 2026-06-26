// Handles client connection to LiveKit video space
async def joinVideoRoom(roomName, scholarIdentity) {
    try {
        const response = await fetch('/api/video/token', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ room_name: roomName, identity: scholarIdentity })
        });
        
        const { token } = await response.json();
        const room = new LiveKitClient.Room();

        // Target rendering node
        const remoteContainer = document.getElementById('remote-video');

        room.on(LiveKitClient.RoomEvent.TrackSubscribed, (track, publication, participant) => {
            if (track.kind === LiveKitClient.Track.Kind.Video || track.kind === LiveKitClient.Track.Kind.Audio) {
                const element = track.attach();
                remoteContainer.appendChild(element);
            }
        });

        const livekitUrl = "wss://your-project.livekit.cloud"; // Fallback or inject dynamically
        await room.connect(livekitUrl, token);
        await room.localParticipant.enableCameraAndMicrophone();
        console.log("Successfully connected to study room:", roomName);

    } catch (error) {
        console.error("Failed to initialize video session:", error);
    }
}

document.getElementById('join-room').addEventListener('click', () => {
    joinVideoRoom('Global-Study-01', `Scholar-${Math.floor(Math.random() * 1000)}`);
});
