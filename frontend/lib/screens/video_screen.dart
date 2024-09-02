import "package:flutter/material.dart";
import "package:tiktourism/widgets/scroll_item.dart";

class VideoScreen extends StatelessWidget {
  const VideoScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView(
        scrollDirection: Axis.vertical,
        children: const [ScrollItem(), ScrollItem()],
      ),
    );
  }
}
