import "package:flutter/material.dart";

class ScrollItem extends StatelessWidget {
  const ScrollItem({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    return Container(
      width: size.width,
      height: size.height,
      decoration: const BoxDecoration(
        color: Colors.black,
      ),
      child: const Image(
        image: NetworkImage(
            "https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg"),
      ),
    );
  }
}
