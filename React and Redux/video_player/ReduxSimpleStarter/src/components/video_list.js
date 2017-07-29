import React from 'react';
import VideoListItem from './video_list_item'

//props contains videos. Functional components (props.) must have it explicitly passed
//class based components have props baked in (this.props.)
const VideoList = (props) => {

    const videoItems = props.videos.map((video) => {
        return <VideoListItem 
                    onVideoSelect={props.onVideoSelect}
                    key={video.etag} 
                    video={video} 
                />
    });

    return (
        <ul className="col-md-4 list-group">
            {videoItems}
        </ul>
    )
}

export default VideoList;